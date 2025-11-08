from langchain_ollama import ChatOllama
from langchain.agents import create_agent

def test_tool(content: str) -> str:
    """Runs the test tool with content as value"""
    return f"Test tool gave {content} is a lie"

llm = ChatOllama(
    model="llama3.2",
    temperature=0.5
)

agent = create_agent(
    llm,
    tools=[test_tool],
    system_prompt="You are a helpful assitant"
)

res = agent.invoke(
    {"messages": [{"role": "user", "content": "Run the test tool on Chicken"}]}
)

print(res["messages"][-1].pretty_print())