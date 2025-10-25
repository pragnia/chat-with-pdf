# 💬 Chat with PDF (Flask + LangChain + Gemini)

Chat with any PDF using Google Gemini and FAISS embeddings!  
This project lets you upload PDFs, extract text (even from scanned files via OCR), and ask natural language questions.

---

## 🚀 Features
- Upload and process multiple PDFs
- OCR support for scanned PDFs
- Vector search with FAISS
- Gemini-powered question answering
- Clean HTML/CSS/JS frontend (no Streamlit)

---



## ⚙️ Setup Instructions

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/chat-with-pdf.git
cd chat-with-pdf


2️⃣ Create a virtual environment

python -m venv .venv
.venv\Scripts\activate    # (Windows)
# OR
source .venv/bin/activate # (Mac/Linux)


3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Add your Google API key

Create a .env file in the project root:

GOOGLE_API_KEY=your_google_api_key_here

5️⃣ Run the Flask app

python app.py
