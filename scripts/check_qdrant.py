from qdrant_client import QdrantClient


def main():

    print("Connecting to Qdrant...")

    client = QdrantClient(path="qdrant_db")

    print("Connected successfully!")

    collection_name = "govdocs"

    if not client.collection_exists(collection_name):
        print("Collection does not exist!")
        return

    collection_info = client.get_collection(collection_name)

    print("\n==============================")
    print("QDRANT COLLECTION")
    print("==============================")

    print("Collection:", collection_name)
    print("Stored vectors:", collection_info.points_count)
    print("Vector size:", collection_info.config.params.vectors.size)


if __name__ == "__main__":
    main()