
from src.RAG.rag_pipeline import answer_question


def main():
    question = "What is the front setback for a residential building on a road 12 metres wide?"

    answer, sources = answer_question(question)

    print("\n===================================")
    print("USER QUESTION")
    print("===================================")
    print(question)

    print("\n===================================")
    print("GENERATED ANSWER")
    print("===================================")
    print(answer)

    print("\n===================================")
    print("SOURCES USED")
    print("===================================")

    for i, source in enumerate(sources, start=1):
        print(f"\nSource {i}")
        print("Document:", source["document_title"])
        print("Page:", source["page"])
        print("Version:", source["version"])
        print("Status:", source["status"])
          
    


if __name__ == "__main__":
    main()