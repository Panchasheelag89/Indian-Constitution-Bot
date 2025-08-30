import os
import google.generativeai as genai
from retriever import search
from vectordb import vector_db

genai.configure(api_key="AIzaSyCxnk0sh4TO-2U2t7OzAfZxVRlm44ID_Mg")

def generate_answer(query, index, chunks, k=2):
    chunk, score = search(query, index, chunks, k)
    context = f"Context:\n{chunk}\n\nQuestion: {query}\nAnswer:"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(context)
    return response.text

if __name__ == "__main__":
    chunks = ["Article 21: Right to life", "Article 19: Freedom of speech"]
    index, embeddings = vector_db(chunks)

    query = "What is Article 21?"
    answer = generate_answer(query, index, chunks, k=1)

    print("Q:", query)
    print("A:", answer)
