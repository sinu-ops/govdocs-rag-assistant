from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from langchain_qdrant import QdrantVectorStore

from src.config import QDRANT_PATH
from src.embeddings.embeddings import get_embeddings


def create_vector_store(documents):

    embeddings = get_embeddings()

    # Persistent local Qdrant database
    client = QdrantClient(path=str(QDRANT_PATH))

    # Create collection if it doesn't exist
    if not client.collection_exists("govdocs"):

        client.create_collection(
            collection_name="govdocs",
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

    # Connect LangChain to Qdrant
    vector_store = QdrantVectorStore(
        client=client,
        collection_name="govdocs",
        embedding=embeddings,
    )

    # Add documents in batches
    batch_size = 100
    total_documents = len(documents)

    for start in range(0, total_documents, batch_size):

        end = min(start + batch_size, total_documents)

        batch = documents[start:end]

        print(
            f"Processing chunks {start + 1}-{end} "
            f"of {total_documents}..."
        )

        vector_store.add_documents(batch)

    return vector_store