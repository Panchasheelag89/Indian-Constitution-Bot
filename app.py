import streamlit as st
import time
from loader import load_pdf
from cleaner import clean_text
from chunks import chunk_text
from vectordb import vector_db
from generator import generate_answer

# Page config
st.set_page_config(
    page_title="Indian Constitution Q&A Chatbot",
    page_icon="📜",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Title & description
st.title("📜 Indian Constitution Q&A Chatbot")
st.write("Ask me anything about the Indian Constitution!")

# Setup
def setup():
    pdf_path = "data/IndianConstitution.pdf"
    raw_text = load_pdf(pdf_path)
    cleaned = clean_text(raw_text)
    chunks = chunk_text(cleaned)
    index, embeddings = vector_db(chunks)
    return index, chunks

index, chunks = setup()

# Sample questions
st.markdown("### 🔍 Try asking me these sample questions:")
sample_questions = [
    "What does the document say about the creation of new states and the alteration of existing ones?",
    "Which articles in the provided text are related to Fundamental Rights?",
    "What is the role of the President regarding bills reserved by a Governor for the President's consideration?",
    "What rights and privileges are given to permanent residents of Jammu & Kashmir by existing laws?"
]
for q in sample_questions:
    st.markdown(f"- {q}")

# User query
query = st.text_input("💬 Enter your question:")

if query:
    # Create a placeholder
    status_placeholder = st.empty()

    # Show "processing" message immediately
    status_placeholder.subheader("⏳ Processing your question...")

    # Simulate progress
    with st.spinner("Searching the Constitution..."):
        time.sleep(1)  # just simulating delay
        answer = generate_answer(query, index, chunks, k=3)

    # Replace placeholder with final answer
    status_placeholder.empty()
    st.subheader("✅ Answer:")
    st.write(answer)
