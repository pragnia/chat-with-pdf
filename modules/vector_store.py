import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


INDEX_PATH = "faiss_index"

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L3-v2",
                                 model_kwargs={'device': 'cpu'} )

def get_vector_store(text_chunks):
    if not text_chunks:
        return None

    embeddings = get_embeddings()
    if not embeddings:
        return None

    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local(INDEX_PATH)

def load_vector_store():
    embeddings = get_embeddings()
    return FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)