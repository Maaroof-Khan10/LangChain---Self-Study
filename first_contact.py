from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen:1.8b",
    temperature=0
)

ai_msg = llm.invoke("What is the current date and time?")
print(ai_msg.content)