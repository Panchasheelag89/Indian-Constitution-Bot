from Pathlib import Path
project_root = path(__file__).resolve().parents[1]
data_dir = project_root/'data'
store_dir = project_root/'store'

embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
chunk_size = 200
chunk_overlap = 100
top_k = 5

Gemini = True
gemini_model = "gemini-1.5-flash"



