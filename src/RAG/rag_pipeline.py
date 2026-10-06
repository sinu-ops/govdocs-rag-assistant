from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
from langchain_qdrant import QdrantVectorStore

from src.config import QDRANT_PATH
from src.embeddings.embeddings import get_embeddings
from src.LLM.llm import get_llm


def get_vector_store():
    client = QdrantClient(path=str(QDRANT_PATH))

    embeddings = get_embeddings()

    vector_store = QdrantVectorStore(
        client=client,
        collection_name="govdocs",
        embedding=embeddings,
    )

    return vector_store


def retrieve_documents(question, k=5):
    vector_store = get_vector_store()

    filter_condition = Filter(
        must=[
            FieldCondition(
                key="metadata.status",
                match=MatchValue(value="current")
            )
        ]
    )

    results = vector_store.similarity_search(
        question,
        k=k,
        filter=filter_condition
    )

    return results


def build_context(documents):
    context_parts = []

    for document in documents:
        context_parts.append(
            f"Source: {document.metadata.get('document_title')}\n"
            f"Page: {document.metadata.get('page_label')}\n"
            f"Content:\n{document.page_content}"
        )

    return "\n\n---\n\n".join(context_parts)


def get_sources(documents):
    sources = []

    for index, document in enumerate(documents, start=1):
        sources.append({
            "source": f"source_{index}",
            "document_title": document.metadata.get("document_title"),
            "page": document.metadata.get("page_label"),
            "version": document.metadata.get("version"),
            "status": document.metadata.get("status"),
            "content": document.page_content,
        })

    return sources


def answer_question(question):
    documents = retrieve_documents(question)

    context = build_context(documents)
    sources=get_sources(documents)

    prompt = f"""
You are a government building regulations assistant.

Answer the user's question using ONLY the provided context.

Rules:
- Give a concise and direct answer.
- Do not create unnecessary tables.
- Do not repeat the entire context.
- Do not invent regulations, numbers, or facts.
- If the context does not contain enough information, say:
  "I could not find a reliable answer in the provided documents."
- Mention the relevant regulation/document when it is clear from the context.

User Question:
{question}

Context:
{context}

Answer:
"""


    llm = get_llm()

    response = llm.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=300,
        temperature=0.1,
    )

    
    
    answer = response.choices[0].message.content

    return answer,sources