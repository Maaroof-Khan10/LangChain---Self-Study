from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
from langchain_core.output_parsers import StrOutputParser

model = OllamaLLM(model="llama3.2")

template = """
You are a assitant for a pizza restaurant. Answer questions based on reviews

Here are some relevant reviews: {reviews}

Here is the question to be answered: {question}
"""

output_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model #| output_parser

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)