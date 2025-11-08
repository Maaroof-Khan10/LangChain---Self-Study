from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="llama3.2",
    temperature=0.5
)

prompt_template = """
Write a small 8 line AABB poem based on {description}.
"""

prompt = PromptTemplate(
    input_variables=["description"],
    template=prompt_template
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print("\nWelcome to bad poem writer\n")
description = input("What should the poem be about> ")
print("\n")

poem = chain.invoke({"description": description})
print(poem)
print("\n")