from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from modules.pdf_utils import get_pdf_text
from modules.text_processing import get_text_chunks
from modules.vector_store import get_vector_store, load_vector_store
from modules.qa_handler import process_user_question
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)
load_dotenv()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_pdfs():
    files = request.files.getlist('pdfs')
    if not files:
        return jsonify({'error': 'No files uploaded'}), 400

    text = get_pdf_text(files)
    chunks = get_text_chunks(text)
    vector = get_vector_store(chunks)
    
    return jsonify({'message': 'PDFs processed successfully!'})


@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    answer = process_user_question(question)
    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=False)
