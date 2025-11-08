# LangChain Self study material
This repo is part of my 3 hour self study sessions where I take one topic and study it for 3 hours

## Notes I made for LangChain (Theory - Questions I try to answer/understand):
1. What is LangChain, and what problem does it solve?\
It is an open-source system that lets developers connect LLMs with documents and tools

2. What are the main building blocks of LangChain?\
Model, Prompts and PromptTemplates, Chains, Agents, Memort and Retrieval.

3. What is a PromptTemplate, and how is it used?\
Reusable prompt with some variable sections that can be changed during runtime to get consistant results.

There are two types of PromptTemplates in lanchain_core .
Basic PromptTemplate and ChatPromptTemplate (better suitable for chat based models)

4. What is an LLMChain, and how does it work?\
Combines an LLM with a Prompt template to recreat reusable workflows.

5. What is the purpose of “Memory” in LangChain?\
Allows model to remember the context of the conversation or task.

6. What is the difference between a “Chain” and an “Agent”?\
Chain is a fixed sequence of actions needed to be performed.
Agents uses LLMs do decide which tools should be used and which action should be performed.

7. What are “Document Loaders” and “Text Splitters” used for?\
Document Loaders load external document creating "document" objects
Text Splitters split these documents into smaller managable chunks

8. What are “Embeddings” and “VectorStores” in LangChain?\
Embedding are the numerical representation of the semantic meaning of words.
VectorStores are the database that stores these numerical embeddings.

9. How do you build a retrieval-augmented generation (RAG) pipeline in LangChain?\
High level overview:
- Load document  
- Split document  
- Embed document  
- Store embeddings
- Choose model  
- Create a prompt template
- Create a chain for RAG

10. What are some common integrations or external tools supported by LangChain?\n
It supports many LLMs, Search engines, web scrappers etc. Could be powerful for creating cool agents

Feel free to correct me or add more stuff if you like.
