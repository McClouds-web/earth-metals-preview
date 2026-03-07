import PyPDF2
import sys

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        return f"Error reading PDF: {e}"

pdf_file = "/Users/tapiwamakore/Downloads/Earth_Metals_Website_Content_Blueprint.pdf"
text_content = extract_text_from_pdf(pdf_file)
with open('pdf_content.txt', 'w', encoding='utf-8') as f:
    f.write(text_content)
print("PDF parsed successfully.")
