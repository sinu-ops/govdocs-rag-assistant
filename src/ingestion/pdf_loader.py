from pathlib import Path

# pyrefly: ignore [missing-import]
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    return loader.load()


def load_all_pdfs(data_path: str):
    data_path = Path(data_path)

    documents = []

    for pdf_file in data_path.rglob("*.pdf"):
        print(f"Loading: {pdf_file}")

        loader = PyPDFLoader(str(pdf_file))
        pdf_documents = loader.load()

        documents.extend(pdf_documents)

    return documents