from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You just have to say 'Hello {name}' to user, nothing else"),
    ("human", "Hi my name is {name}!")
])

prompt_value = chat_template.invoke({"name": "Gaitonde"})

llm = ChatOllama(
    model="qwen:1.8b",
    temperature=0
)

res = llm.invoke(prompt_value)
print(res.content)