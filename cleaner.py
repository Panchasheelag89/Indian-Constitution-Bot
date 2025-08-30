import re
from pathlib import Path
from loader import load_pdf

def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)   # replace multiple spaces/newlines with single space
    return text.strip()                # remove leading/trailing spaces

if __name__ == "__main__":
    pdf_path = Path(r"D:\PROJECTS\Legal_Chatbot\IndianConstitution.pdf")
    raw_text = load_pdf(pdf_path)

    print("\nBefore cleaning:\n", raw_text[:100])   # preview first 100 chars before cleaning

    cleaned = clean_text(raw_text)

    print("\nAfter cleaning:\n", cleaned[:100])    # preview first 100 chars after cleaning
