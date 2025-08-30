from pathlib import Path
from PyPDF2 import PdfReader

def load_pdf(path):
    reader = PdfReader(path)        # open the PDF → reader object
    all_pages = []
    for page in reader.pages:       # loop through each page
        page_text = page.extract_text()
        if page_text:               # only add if text exists
            all_pages.append(page_text)
    return "\n".join(all_pages)     # ✅ no comma here, only a string is returned

if __name__ == "__main__":
    pdf_path = Path(r"D:\PROJECTS\Legal_Chatbot\IndianConstitution.pdf")
    text = load_pdf(pdf_path)
    print(text[:20])    # show first 20 characters
