from src.ingestion.pipeline import run_ingestion


def main():

    data_path = "data/raw"

    chunks = run_ingestion(data_path)

    print("\n===================================")
    print("PIPELINE TEST")
    print("===================================")

    print("Total chunks:", len(chunks))

    print("\n--- First Chunk ---")

    print("\nContent:")
    print(chunks[0].page_content[:1000])

    print("\nMetadata:")
    print(chunks[0].metadata)


if __name__ == "__main__":
    main()