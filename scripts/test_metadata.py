from src.ingestion.pdf_loader import load_pdf
from src.ingestion.cleaner import clean_documents
from src.ingestion.chunker import chunk_documents
from src.ingestion.metadata import add_document_metadata


def main():

    pdf_path = "data/raw/current/UDCPR_2020_updated_2025.pdf"

    print("Loading PDF...")

    documents = load_pdf(pdf_path)

    # Use only first 5 pages for testing
    documents = documents[:5]

    print("Cleaning documents...")

    documents = clean_documents(documents)

    print("Creating chunks...")

    chunks = chunk_documents(documents)

    print("Adding metadata...")

    chunks = add_document_metadata(
        chunks,
        document_id="udcpr_2020",
        document_title="Unified Development Control and Promotion Regulations",
        authority="Government of Maharashtra",
        version="UDCPR 2020",
        status="current"
    )

    print("\n==============================")
    print("METADATA TEST")
    print("==============================")

    print("Total chunks:", len(chunks))

    print("\n--- First Chunk Metadata ---")

    print(chunks[0].metadata)

    print("\n--- First Chunk Content ---")

    print(chunks[0].page_content[:500])


if __name__ == "__main__":
    main()