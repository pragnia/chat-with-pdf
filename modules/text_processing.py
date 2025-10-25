from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    return chunks
