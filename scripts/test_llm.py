from src.LLM.llm import get_llm


def main():
    client = get_llm()

    question = "What is 2 + 2?"

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        max_tokens=100,
        temperature=0.1,
    )

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()