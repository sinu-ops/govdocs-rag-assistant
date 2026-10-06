from langchain_community import document_loaders
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(document):
    "split docs into chunks"

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks=splitter.split_documents(document)
    return chunks

