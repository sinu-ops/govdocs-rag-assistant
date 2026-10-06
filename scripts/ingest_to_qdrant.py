from src.config import DATA_PATH
from src.ingestion.pipeline import run_ingestion
from src.vector_store.qdrant_store import create_vector_store


def main():

    print("===================================")
    print("STARTING QDRANT INGESTION")
    print("===================================")

    # Step 1: Process all PDFs
    print("\nRunning ingestion pipeline...")

    chunks = run_ingestion(str(DATA_PATH))

    print("\nChunks ready:", len(chunks))

    # Step 2: Store chunks in Qdrant
    print("\nCreating persistent Qdrant vector store...")

    vector_store = create_vector_store(chunks)

    print("\n===================================")
    print("QDRANT INGESTION COMPLETE")
    print("===================================")


if __name__ == "__main__":
    main()