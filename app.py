import streamlit as st
from loader import load_pdf
from cleaner import clean_text
from chunks import chunk_text
from vectordb import vector_db
from retriever import search
from generator import generate_answer

def setup():
    pdf_path = "data/IndianConstitution.pdf"
    raw_text = load_pdf(pdf_path)
    cleaned = clean_text(raw_text)
    chunks = chunk_text(cleaned)
    index, embeddings = vector_db(chunks)
    return index, chunks

st.title(" Indian Constitution Q&A Chatbot")
st.write("Ask questions about the Indian Constitution!")

# Load index & chunks
index, chunks = setup()

# User query
query = st.text_input("Enter your question:")

if query:
    answer = generate_answer(query, index, chunks, k=3)
    st.subheader("Answer:")
    st.write(answer)
