import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from src.config import ENV_PATH

load_dotenv(ENV_PATH)


def get_llm():
    api_key = os.getenv("HF_TOKEN")

    if not api_key:
        raise RuntimeError(
            f"HF_TOKEN is not set. Add it to {ENV_PATH} (or the environment)."
        )

    client = InferenceClient(
        api_key=api_key,
        provider="auto",
    )

    return client


def format_context(retrieved_docs):
    formatted = "\n\n".join([d.page_content for d in retrieved_docs])

    return formatted