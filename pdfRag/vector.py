from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

if add_documents:
    loader = PyPDFLoader("test.pdf")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunked_docs = text_splitter.split_documents(docs)

vector_store = Chroma(
    collection_name="research_paper",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(chunked_docs)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 10}
)