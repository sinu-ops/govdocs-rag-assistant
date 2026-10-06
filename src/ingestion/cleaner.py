import re


def clean_documents(documents):
    """
    Clean the page_content of LangChain Documents
    while preserving their metadata.
    """

    cleaned_documents = []

    for document in documents:

        text = document.page_content

        # Normalize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Remove trailing spaces from each line
        lines = [line.rstrip() for line in text.split("\n")]

        # Remove repeated blank lines
        cleaned_lines = []
        previous_blank = False

        for line in lines:

            if not line.strip():

                if not previous_blank:
                    cleaned_lines.append("")

                previous_blank = True

            else:

                cleaned_lines.append(line)
                previous_blank = False

        text = "\n".join(cleaned_lines)

        # Remove repeated spaces/tabs
        text = re.sub(r"[ \t]+", " ", text)

        # Remove excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        document.page_content = text.strip()

        cleaned_documents.append(document)

    return cleaned_documents