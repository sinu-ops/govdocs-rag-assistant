from src.ingestion.pipeline import run_ingestion


def main():

    print("Loading and chunking documents...")

    chunks = run_ingestion("data/raw")

    print("\n===================================")
    print("CHUNK INSPECTION")
    print("===================================")

    # Inspect chunks related to setback
    matching_chunks = []

    for chunk in chunks:

        text = chunk.page_content.lower()

        if "setback" in text:

            matching_chunks.append(chunk)

    print("\nChunks containing 'setback':", len(matching_chunks))

    # Show first 10 matching chunks
    for i, chunk in enumerate(matching_chunks[:10], start=1):

        print(f"\n{'=' * 70}")
        print(f"CHUNK {i}")
        print(f"{'=' * 70}")

        print("\nDocument:")
        print(chunk.metadata.get("document_id"))

        print("Page:")
        print(chunk.metadata.get("page_label"))

        print("\nContent:")
        print(chunk.page_content[:1500])


if __name__ == "__main__":
    main()