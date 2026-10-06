from src.ingestion.pdf_loader import load_pdf


def main():

    print("Starting PDF loading...")

    pdf_path = "data/raw/current/UDCPR_2020_updated_2025.pdf"

    documents = load_pdf(pdf_path)

    print("PDF loaded successfully!")
    print("Total pages:", len(documents))

    print("\n--- First page ---")
    print(documents[0].page_content[:1000])

    print("\n--- Metadata ---")
    print(documents[0].metadata)


if __name__ == "__main__":
    main()