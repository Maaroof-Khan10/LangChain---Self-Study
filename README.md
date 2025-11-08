# LangChain Self study material
This repo is part of my 3 hour self study sessions where I take one topic and study it for 3 hours

## Notes I made for LangChain (Theory):
What is LangChain, and what problem does it solve?
It is an open-source system that lets developers connect LLMs with documents and tools

What are the main building blocks of LangChain?
Model, Prompts and PromptTemplates, Chains, Agents, Memort and Retrieval

What is a PromptTemplate, and how is it used?
Reusable prompt with some variable sections that can be changed during runtime to get consistant results

There are two types of PromptTemplates in lanchain_core 
Basic PromptTemplate and ChatPromptTemplate (better suitable for chat based models)

What is an LLMChain, and how does it work?
Combines an LLM with a Prompt template to recreat reusable workflows

What is the purpose of “Memory” in LangChain?
Allows model to remember the context of the conversation or task

What is the difference between a “Chain” and an “Agent”?
Chain is a fixed sequence of actions needed to be performed
Agents uses LLMs do decide which tools should be used and which action should be performed

What are “Document Loaders” and “Text Splitters” used for?
Document Loaders load external document creating "document" objects
Text Splitters split these documents into smaller managable chunks

What are “Embeddings” and “VectorStores” in LangChain?
Embedding are the numerical representation of the semantic meaning of words 
VectorStores are the database that stores these numerical embeddings

How do you build a retrieval-augmented generation (RAG) pipeline in LangChain?

High level overview:
1. Load document
2. Split document
3. Embed document
4. Store embeddings
5. Choose model
6. Create a prompt template
7. Create a chain for RAG

What are some common integrations or external tools supported by LangChain?
It supports many LLMs, Search engines, web scrappers etc. Could be powerful for creating cool agents
