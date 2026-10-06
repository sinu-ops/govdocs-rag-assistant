from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
from langchain_qdrant import QdrantVectorStore

from src.embeddings.embeddings import get_embeddings 


def main():

    print("Connecting to Qdrant...")

    client = QdrantClient(path="qdrant_db")

    embeddings = get_embeddings()

    vector_store = QdrantVectorStore(
        client=client,
        collection_name="govdocs",
        embedding=embeddings,
    )

    query = "What is the front setback for a residential building on a road 12 metres wide?"

    print("\n===================================")
    print("CURRENT DOCUMENT SEARCH")
    print("===================================")

    print("\nQuery:")
    print(query)

    # Search only current documents
    filter_condition = Filter(
    must=[
        FieldCondition(
            key="metadata.status",
            match=MatchValue(value="current")
        )
    ]
)

    results = vector_store.similarity_search_with_score(
    query,
    k=10,
    filter=filter_condition
)

    seen=set()
    unique_result=[]
    for result,score in results:
        text=result.page_content
        if text not in seen:
            seen.add(text)
            unique_result.append((result,score))
        


    print("\n===================================")
    print("SEARCH RESULTS")
    print("===================================")

    for i, (result, score) in enumerate(unique_result, start=1):

        print(f"\n{'=' * 60}")
        print(f"RESULT {i}")
        print(f"{'=' * 60}")

        print("\nScore:")
        print(score)

        print("\nContent:")
        print(result.page_content[:1000])

        print("\nMetadata:")
        print(result.metadata)


if __name__ == "__main__":
    main()