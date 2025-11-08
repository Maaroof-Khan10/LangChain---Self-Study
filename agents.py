from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from datetime import datetime

def get_current_time():
    """Get the current date and time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

agent = create_agent(llm, tools=[get_current_time])

query = input("\nAsk a question> ")

res = agent.invoke({"messages": [{"role": "user", "content": query}]})
print(res["messages"][-1].content)