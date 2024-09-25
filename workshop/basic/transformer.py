from sentence_transformers import SentenceTransformer

def get_sentence_embeddings(sentences):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences, clean_up_tokenization_spaces=True)
    return embeddings

if __name__ == "__main__":
    sentences = ["I love dogs", "I like cats"]
    embeddings = get_sentence_embeddings(sentences)
    print(embeddings)