import chromadb
import pandas as pd
import streamlit as st
import argparse

parser = argparse.ArgumentParser(
    description="Set the Chroma DB path to view collections"
)
parser.add_argument("db")

pd.set_option("display.max_columns", 4)


def view_collections(dir):
    st.markdown("### DB Path: %s" % dir)

    client = chromadb.PersistentClient(path=dir)

    # This might take a while in the first execution if Chroma wants to download
    # the embedding transformer
    print(client.list_collections())

    st.header("Collections")

    for coll in client.list_collections():
        print("getting data for collection: %s" % coll)
        collection = client.get_collection(
            coll,
        )
       
        data = collection.get(include=["embeddings"])
        print(data)
        ids = data["ids"]
        embeddings = data["embeddings"]
        data = collection.get()
        metadata = data["metadatas"]
        documents = data["documents"]
        
        # Show in table
        st.write("Collection: %s" % coll)
        st.write(pd.DataFrame(zip(documents, embeddings), columns=['Documents', 'Embeddings']))
        st.write("Total documents: %d" % len(documents))

if __name__ == "__main__":
    try:
        args = parser.parse_args()
        print("Opening database: %s" % args.db)
        view_collections(args.db)
    except Exception as e:
        print("An error occurred: %s" % str(e))
        pass
