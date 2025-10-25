from modules.vector_store import load_vector_store
from modules.conversational_chain import get_conversational_chain

def process_user_question(user_question):
    db = load_vector_store()
    docs = db.similarity_search(user_question)

    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

    return response["output_text"]
