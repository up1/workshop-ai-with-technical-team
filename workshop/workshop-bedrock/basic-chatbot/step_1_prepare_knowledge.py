from load_data import load_pdfs
from create_vector import create_vector_store

if __name__ == "__main__":
    docs = load_pdfs()
    create_vector_store(docs=docs)