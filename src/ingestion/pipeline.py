from src.ingestion.pdf_loader import load_all_pdfs
from src.ingestion.cleaner import clean_documents
from src.ingestion.chunker import chunk_documents
from src.ingestion.metadata import add_document_metadata


def run_ingestion(data_path):

    print("===================================")
    print("STARTING INGESTION PIPELINE")
    print("===================================")

    # Step 1: Load PDFs
    print("\n[1/4] Loading PDFs...")

    documents = load_all_pdfs(data_path)

    print("Total pages loaded:", len(documents))

    # Step 2: Clean
    print("\n[2/4] Cleaning documents...")

    documents = clean_documents(documents)

    print("Cleaning completed.")

    # Step 3: Chunk
    print("\n[3/4] Creating chunks...")

    chunks = chunk_documents(documents)

    print("Total chunks created:", len(chunks))

    # Step 4: Add metadata
    print("\n[4/4] Adding metadata...")

    chunks = add_document_metadata(chunks)

    print("Metadata added.")

    print("\n===================================")
    print("INGESTION COMPLETED")
    print("===================================")

    return chunks