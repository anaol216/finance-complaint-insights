import pandas as pd
import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from tqdm import tqdm
import os

class ComplaintEmbedder:
    def __init__(self, model_name="all-MiniLM-L6-v2", chunk_size=300, chunk_overlap=50):
        self.model = SentenceTransformer(model_name)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ".", " ", ""]
        )
        self.chunks = []
        self.metadata = []

    def load_data(self, filepath):
        return pd.read_csv(filepath)

    def chunk_complaints(self, df):
        for _, row in tqdm(df.iterrows(), total=len(df)):
            chunks = self.text_splitter.split_text(row["cleaned_narrative"])
            for i, chunk in enumerate(chunks):
                self.chunks.append(chunk)
                self.metadata.append({
                    "complaint_id": row["Complaint ID"],
                    "product": row["Product"],
                    "chunk_index": i
                })

    def embed_chunks(self):
        return self.model.encode(self.chunks, show_progress_bar=True, convert_to_numpy=True)

    def build_vector_store(self, embeddings, save_path="vector_store"):
        os.makedirs(save_path, exist_ok=True)

        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)

        faiss.write_index(index, os.path.join(save_path, "faiss_index.index"))

        with open(os.path.join(save_path, "chunk_metadata.pkl"), "wb") as f:
            pickle.dump(self.metadata, f)

        print(f"Vector store saved to `{save_path}`")

    def run(self, data_path, save_path="vector_store"):
        df = self.load_data(data_path)
        self.chunk_complaints(df)
        embeddings = self.embed_chunks()
        self.build_vector_store(embeddings, save_path)


if __name__ == "__main__":
    embedder = ComplaintEmbedder()
    embedder.run("data/filtered_complaints.csv")
