from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def get_embeddings():
    return OpenAIEmbeddings(model="text-embedding-3-small")

def get_vector_store(text_chunks):
    embeddings = get_embeddings()
    vectorstore = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vectorstore
