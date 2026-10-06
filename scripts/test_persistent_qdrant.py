from qdrant_client import QdrantClient


def main():

    print("Connecting to persistent Qdrant...")

    client = QdrantClient(path="qdrant_db")

    print("Connected successfully!")

    if client.collection_exists("govdocs"):
        print("Collection 'govdocs' exists.")
    else:
        print("Collection 'govdocs' does not exist yet.")


if __name__ == "__main__":
    main()