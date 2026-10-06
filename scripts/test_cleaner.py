from src.ingestion.pdf_loader import load_pdf
from src.ingestion.cleaner import clean_documents


def main():

    pdf_path = "data/raw/current/UDCPR_2020_updated_2025.pdf"

    print("Loading PDF...")

    documents = load_pdf(pdf_path)

    # Test only first 5 pages
    documents = documents[:5]

    print("Cleaning documents...")

    cleaned_documents = clean_documents(documents)

    print("\nCleaning complete!")
    print("Documents cleaned:", len(cleaned_documents))

    first_document = cleaned_documents[0]

    print("\n--- Cleaned Content ---")
    print(first_document.page_content[:1000])

    print("\n--- Metadata ---")
    print(first_document.metadata)


if __name__ == "__main__":
    main()