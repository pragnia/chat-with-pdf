from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract
import tempfile
import os

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        pdf_text = ""
        for page in pdf_reader.pages:
            pdf_text += page.extract_text() or ""

        if not pdf_text.strip():
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(pdf.read())
                temp_pdf.flush()
                pdf_text = extract_text_with_ocr(temp_pdf.name)
                os.unlink(temp_pdf.name)

        text += pdf_text
    return text


def extract_text_with_ocr(pdf_path):
    print("🧠 Running OCR on scanned PDF...")
    pages = convert_from_path(pdf_path)
    text = ""
    for i, page in enumerate(pages):
        print(f"Processing page {i+1}/{len(pages)} via OCR...")
        text += pytesseract.image_to_string(page)
    return text