import faiss
import numpy as np
from embedding import get_embedding


def vector_db(chunks):
    embeddings=[]
    for chunk in chunks:
        emd= get_embedding(chunk)
        embeddings.append(emd)
    embeddings = np.array(embeddings).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, embeddings

if __name__== "__main__":
        chunks = ["Article 21: Right to life", "Article 19: Freedom of speech"]
        index, embeddings = vector_db(chunks)
        print("chunks:",chunks[:3])
        print("total_chunks:",len(chunks))
        print("embeddings_shape:",embeddings.shape)

    