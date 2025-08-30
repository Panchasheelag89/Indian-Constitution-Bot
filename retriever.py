import numpy as np
from embedding import get_embedding
from vectordb import vector_db   

def search(query, index, chunks, k=2):
    query_embedding = np.array([get_embedding(query)], dtype="float32")
    distances, indices = index.search(query_embedding, k)

    first_chunk = chunks[indices[0][0]]
    first_score = distances[0][0]

    return first_chunk, first_score

if __name__ == "__main__":
    chunks = ["Article 21: Right to life", "Article 19: Freedom of speech"]

    index, embeddings = vector_db(chunks)

    query = "right to life"
    chunk, score = search(query, index, chunks, k=1)

    print("Query:", query)
    print("Best match:", chunk)
    print("Score:", score)
