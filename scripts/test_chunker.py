from src.ingestion.pdf_loader import load_pdf
from src.ingestion.cleaner import clean_documents
from src.ingestion.chunker import chunk_documents


def main():

    pdf_path = "data/raw/current/UDCPR_2020_updated_2025.pdf"

    print("Loading PDF...")

    documents = load_pdf(pdf_path)

    # Test only first 5 pages
    documents = documents[:5]

    print("Cleaning documents...")

    documents = clean_documents(documents)

    print("Creating chunks...")

    chunks = chunk_documents(documents)

    print("\n==============================")
    print("CHUNKING COMPLETE")
    print("==============================")

    print("Original documents:", len(documents))
    print("Total chunks:", len(chunks))

    for i, chunk in enumerate(chunks[:5], start=1):

        print("\n" + "=" * 60)
        print(f"CHUNK {i}")
        print("=" * 60)

        print("Characters:", len(chunk.page_content))

        print("\nMetadata:")
        print(chunk.metadata)

        print("\nContent:")
        print(chunk.page_content[:500])


if __name__ == "__main__":
    main()