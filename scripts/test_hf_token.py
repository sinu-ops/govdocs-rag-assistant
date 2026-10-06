import os

from dotenv import load_dotenv


load_dotenv()


def main():

    token = os.getenv("HF_TOKEN")

    if token:
        print("HF_TOKEN loaded successfully!")
        print("Token starts with:", token[:3])
    else:
        print("HF_TOKEN not found!")


if __name__ == "__main__":
    main()