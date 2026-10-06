from src.embeddings.embeddings import get_embeddings


def main():

    print("Loading embedding model...")

    embeddings = get_embeddings()

    text = "What is the minimum setback required for a building?"

    print("\nCreating embedding...")

    vector = embeddings.embed_query(text)

    print("\nEmbedding created!")
    print("Vector dimensions:", len(vector))
    print("First 10 values:", vector[:10])


if __name__ == "__main__":
    main()