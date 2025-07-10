import os
import pickle
from typing import List, Dict

import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
from transformers.pipelines import pipeline

# === Load Resources ===
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
INDEX_PATH = "vector_store/faiss_index.index"
METADATA_PATH = "vector_store/chunk_metadata.pkl"

# Load vector store
index = faiss.read_index(INDEX_PATH)

# Load metadata (e.g., complaint_id, product, original_text)
with open(METADATA_PATH, "rb") as f:
    metadata = pickle.load(f)

# Load embedding model
embedder = SentenceTransformer(EMBEDDING_MODEL_NAME)

# Load generator model (can be changed to OpenAI / Mistral if needed)
generator = pipeline("text-generation", model="gpt2", max_new_tokens=200)

# === RAG Core ===

def retrieve_relevant_chunks(query: str, top_k: int = 5) -> List[Dict]:
    """
    Embed the query and retrieve top-k most similar chunks from FAISS.
    """
    query_embedding = embedder.encode([query])
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for i in indices[0]:
        results.append(metadata[i])
    return results

for i, chunk in enumerate(metadata[:10], 1):  # Check first 10 chunks
    print(f"\n--- Chunk {i} ---")
    print("Keys:", chunk.keys())
    print("Content Preview:")
    
    # Try printing common keys if they exist
    if "page_content" in chunk:
        print("page_content:", chunk["page_content"][:300])
    elif "text" in chunk:
        print("text:", chunk["text"][:300])
    else:
        print("No known text content found.")

def format_prompt(context_chunks: List[Dict], question: str) -> str:
    """
    Combine context and question into a single prompt for the LLM.
    """
    context_text = "\n\n".join(chunk["page_content"] for chunk in context_chunks)

    prompt = f"""You are a financial analyst assistant for CrediTrust.
Your task is to answer questions about customer complaints.
Use the following retrieved complaint excerpts to formulate your answer.
If the context doesn't contain the answer, say you don't have enough information.

Context:
{context_text}

Question: {question}
Answer:"""

    return prompt


def generate_answer(prompt: str) -> str:
    """
    Use a language model to generate a response based on the prompt.
    """
    output = generator(prompt, return_full_text=False)
    return output[0]['generated_text'].strip()


def rag_answer(query: str, top_k: int = 5) -> Dict:
    """
    Full RAG pipeline: embed, retrieve, prompt, generate.
    """
    chunks = retrieve_relevant_chunks(query, top_k=top_k)
    prompt = format_prompt(chunks, query)
    answer = generate_answer(prompt)

    return {
        "question": query,
        "answer": answer,
        "sources": chunks
    }


# === CLI Example ===
if __name__ == "__main__":
    sample_question = "Why are customers complaining about Buy Now Pay Later?"
    result = rag_answer(sample_question)

    print("\n--- Question ---")
    print(result["question"])

    print("\n--- Answer ---")
    print(result["answer"])

    print("\n--- Top Sources ---")
    for i, src in enumerate(result["sources"], 1):
        print(f"\n[{i}] Product: {src['product']}\nText: {src['text'][:300]}...")
