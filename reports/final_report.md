
---

# 10 Academy: Artificial Intelligence Mastery

CrediTrust Financial Complaint Intelligence – INTERIM REPORT – Week 1 Challenge
Name: ANAOL ATINAFU
Email: [atinafuanaol@gmail.com](mailto:atinafuanaol@gmail.com)
Project: Intelligent Complaint Analysis for Financial Services
Organization: CrediTrust Financial / 10 Academy
Date: July 10, 2025A

---

## 📌 Introduction

CrediTrust Financial, an East African fintech provider, receives thousands of monthly customer complaints in unstructured form. Manual review is time-consuming and inefficient for product managers, compliance officers, and support teams.

To solve this, we built an AI-powered assistant using **Retrieval-Augmented Generation (RAG)** to surface strategic insights from complaint narratives. This system allows non-technical users to query in plain English and receive synthesized answers with context.

---

## 🧹 Task 1: Data Cleaning and Exploration

### Source  
- Dataset: Consumer Financial Protection Bureau (CFPB)  
- Products included:
  - Credit Card  
  - Personal Loan  
  - Buy Now, Pay Later (BNPL)  
  - Savings Account  
  - Money Transfers  

### Key Cleaning Steps  
- Filtered missing complaint narratives  
- Lowercased text  
- Removed boilerplate and special characters  
- Normalized whitespace  
- Saved cleaned file: `data/filtered_complaints.csv`

### EDA Highlights  
- BNPL and Credit Card had the highest complaint volume  
- Narrative length ranged from 10 to 500+ words  
- Over 40% of records lacked narrative and were removed  

---

## 🔗 Task 2: Chunking, Embedding, and Indexing

### Chunking Strategy  

- Used LangChain’s `RecursiveCharacterTextSplitter`  
- Parameters:
  - `chunk_size = 300`  
  - `chunk_overlap = 100`  

### Embedding Model 

- `sentence-transformers/all-MiniLM-L6-v2`  
- Chosen for its balance of accuracy and efficiency  

### Vector Indexing with FAISS  

- Stored 170,000+ vector chunks  
- Metadata includes complaint ID, product, and chunk text  
- Index saved at `vector_store/faiss_index.index`  
- Chunk metadata saved at `vector_store/chunk_metadata.pkl`

---

## 🧠 Task 3: RAG Pipeline and Evaluation

### Architecture  

- **Retriever:** FAISS + SentenceTransformer for top-k semantic matches  
- **Prompt Constructor:** Injects retrieved chunks into LLM prompt  
- **Generator:** GPT-2 (local) or optionally HuggingFace/OpenAI API  

### Sample Prompt  

You are a financial analyst assistant for CrediTrust.
Use the following complaint excerpts to answer the question.
If the context doesn’t include the answer, say you don't have enough information.

Context:
{chunked_texts}

Question: Why are customers unhappy with Buy Now Pay Later?

### Evaluation Table

| Question | Generated Answer | Chunks Used | Score (1–5) | Comments |
|----------|------------------|-------------|-------------|----------|
| Why are people complaining about BNPL? | Late fees and refund delays |  | 5 | Strong evidence |
| What's the most common Credit Card issue? | Hidden fees and credit limit errors |  | 4 | Good summary |
| Are there complaints about fund delays? | Yes, mostly with transfers |  | 5 | Relevant |
| Do responses vary over time? | Not enough information | | 2 | Lacks temporal filtering |
| Is customer service mentioned? | Not frequently |  | 3 | Needs better context linking |

---

## 💬 Task 4: Interactive Chat UI

### Features  
- Built with **Streamlit** (`app.py`)  
- Real-time RAG-based Q&A from complaint data  
- Input box + "Submit" button  
- Displays LLM answer + source chunks  
- "Clear" button resets the interface  
- Sources shown to enhance user trust  

### Deployment  
To launch:
```bash
streamlit run app.py

Here’s the complete content for your `final_report.md`, formatted in Markdown and based on your completed Week 6 project. This file is ideal for submission and also works well as a GitHub project summary or portfolio artifact.

---

```markdown
# 🧠 10 Academy – Week 6: Final Report  
## CrediTrust Complaint Intelligence – Retrieval-Augmented Generation (RAG) System  
**Author:** Anaol Atinafu  
**Email:** atinafuanaol@gmail.com  
**Organization:** CrediTrust Financial / 10 Academy  
**Date:** July 8, 2025  

---

## 📌 Introduction

CrediTrust Financial, an East African fintech provider, receives thousands of monthly customer complaints in unstructured form. Manual review is time-consuming and inefficient for product managers, compliance officers, and support teams.

To solve this, we built an AI-powered assistant using **Retrieval-Augmented Generation (RAG)** to surface strategic insights from complaint narratives. This system allows non-technical users to query in plain English and receive synthesized answers with context.

---

## 🧹 Task 1: Data Cleaning and Exploration

### Source  
- Dataset: Consumer Financial Protection Bureau (CFPB)  
- Products included:
  - Credit Card  
  - Personal Loan  
  - Buy Now, Pay Later (BNPL)  
  - Savings Account  
  - Money Transfers  

### Key Cleaning Steps  
- Filtered missing complaint narratives  
- Lowercased text  
- Removed boilerplate and special characters  
- Normalized whitespace  
- Saved cleaned file: `data/filtered_complaints.csv`

### EDA Highlights  
- BNPL and Credit Card had the highest complaint volume  
- Narrative length ranged from 10 to 500+ words  
- Over 40% of records lacked narrative and were removed  

---

## 🔗 Task 2: Chunking, Embedding, and Indexing

### Chunking Strategy  
- Used LangChain’s `RecursiveCharacterTextSplitter`  
- Parameters:
  - `chunk_size = 300`  
  - `chunk_overlap = 100`  

### Embedding Model  
- `sentence-transformers/all-MiniLM-L6-v2`  
- Chosen for its balance of accuracy and efficiency  

### Vector Indexing with FAISS  
- Stored 170,000+ vector chunks  
- Metadata includes complaint ID, product, and chunk text  
- Index saved at `vector_store/faiss_index.index`  
- Chunk metadata saved at `vector_store/chunk_metadata.pkl`

---

## 🧠 Task 3: RAG Pipeline and Evaluation

### Architecture  
- **Retriever:** FAISS + SentenceTransformer for top-k semantic matches  
- **Prompt Constructor:** Injects retrieved chunks into LLM prompt  
- **Generator:** GPT-2 (local) or optionally HuggingFace/OpenAI API  

### Sample Prompt  
```

You are a financial analyst assistant for CrediTrust.
Use the following complaint excerpts to answer the question.
If the context doesn’t include the answer, say you don't have enough information.

Context:
{chunked\_texts}

Question: Why are customers unhappy with Buy Now Pay Later?

Answer:

````

### Evaluation Table

| Question | Generated Answer | Chunks Used | Score (1–5) | Comments |
|----------|------------------|-------------|-------------|----------|
| Why are people complaining about BNPL? | Late fees and refund delays  | 5 | Strong evidence |
| What's the most common Credit Card issue? | Hidden fees and credit limit errors || 4 | Good summary |
| Are there complaints about fund delays? | Yes, mostly with transfers  | 5 | Relevant |
| Do responses vary over time? | Not enough information | 2 | Lacks temporal filtering |
| Is customer service mentioned? | Not frequently || 3 | Needs better context linking |

---

## 💬 Task 4: Interactive Chat UI

### Features  
- Built with **Streamlit** (`app.py`)  
- Real-time RAG-based Q&A from complaint data  
- Input box + "Submit" button  
- Displays LLM answer + source chunks  
- "Clear" button resets the interface  
- Sources shown to enhance user trust  

### Deployment  
To launch:
```bash
streamlit run app.py
````

### Screenshot

(Screenshot added to GitHub README)

---

## 🔍 Challenges and Solutions

| Challenge          | Solution                          |
| ------------------ | --------------------------------- |
| Missing narratives | Filtered at preprocessing stage   |
| Long text          | Chunked using LangChain splitters |
| Embedding latency  | Used batch encoding with tqdm     |
| Push errors        | Large files tracked using DVC     |
| FAISS mismatch     | Fixed metadata and chunk keys     |

---

## ✅ Recommendations

1. Replace GPT-2 with instruction-tuned model (e.g., Mistral, OpenChat, LLaMA 3)
2. Add product/date filters in the frontend
3. Deploy via Streamlit Cloud or Hugging Face Spaces
4. Extend dataset to include company response metadata
5. Add Amharic support and sentiment classification

---

## 📁 Repository Overview

| File/Folder                         | Description                  |
| ----------------------------------- | ---------------------------- |
| `data/filtered_complaints.csv`      | Cleaned complaint data       |
| `vector_store/faiss_index.index`    | FAISS vector index           |
| `vector_store/chunk_metadata.pkl`   | Chunk-level metadata         |
| `src/embedding_indexer.py`          | Chunk and embed complaints   |
| `src/rag_pipeline.py`               | Full RAG implementation      |
| `app.py`                            | Streamlit user interface     |
| `notebooks/eda_preprocessing.ipynb` | EDA and cleaning             |
| `requirements.txt`                  | Project dependencies         |
| `README.md`                         | Instructions and usage guide |

---

## 🏁 Conclusion

This project showcases how a combination of NLP techniques—semantic search, embeddings, and LLMs—can transform messy complaint data into actionable intelligence.

The final RAG system enables product and compliance teams to ask natural questions like:

* *“Why are customers unhappy with BNPL?”*
* *“What issues are frequent in money transfers?”*

And get clear answers in seconds—grounded in real customer narratives.

The system is modular, scalable, and ready for deployment across CrediTrust’s customer operations.

---
