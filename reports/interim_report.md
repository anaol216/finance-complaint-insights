
---

# 10 Academy: Artificial Intelligence Mastery

CrediTrust Financial Complaint Intelligence – INTERIM REPORT – Week 1 Challenge
Name: ANAOL ATINAFU
Email: [atinafuanaol@gmail.com](mailto:atinafuanaol@gmail.com)
Project: Intelligent Complaint Analysis for Financial Services
Organization: MoonLight Energy Solutions / 10 Academy
Date: July 6, 2025

---

## Introduction

CrediTrust Financial operates across East Africa, serving over 500,000 users across credit cards, personal loans, BNPL, savings, and transfers. Every month, thousands of unstructured complaints arrive through multiple channels. Currently, key teams—Product, Support, and Compliance—manually comb through these narratives, wasting time and missing patterns.

This report details the first phase in building an internal AI system that transforms raw complaints into actionable insights using a Retrieval-Augmented Generation (RAG) pipeline. The goal is simple: turn feedback into foresight.

---

## Task 1: Exploratory Data Analysis and Preprocessing

### Dataset Overview

The dataset comes from the Consumer Financial Protection Bureau (CFPB) and includes:

* Product category
* Complaint issue
* Narrative (free text)
* Company name
* Submission timestamp
* Metadata for tracking

### Key Activities

* Loaded over 500K complaint records from `complaints.csv`
* Filtered records to 5 core products: Credit Card, Personal Loan, BNPL, Savings Account, Money Transfers
* Removed complaints with empty narratives (over 50% of raw records)
* Analyzed:

  * Complaint distribution by product
  * Narrative length (word count distribution)
  * Missingness patterns
* Cleaned narratives using:

  * Lowercasing
  * Removal of special characters, emails, boilerplate phrases
  * Optional whitespace and stopword removal

### EDA Insights

* BNPL and Credit Cards lead in volume, revealing hot pain points
* Narrative lengths ranged from 5 to 700+ words, with a sweet spot around 100
* Many complaints were vague or overly templated—cleaning drastically improved quality
* Final dataset saved to: `data/filtered_complaints.csv`

---

## Task 2: Text Chunking, Embedding and Indexing

### Why Chunk?

Large narratives don’t embed well as single vectors. We used LangChain’s `RecursiveCharacterTextSplitter` to chunk narratives into overlapping text blocks that retain semantic context.

* Chunk size: 300 characters
* Overlap: 100 characters

This ensures the model captures full issues without truncating meaning.

### Embedding Model

We used `sentence-transformers/all-MiniLM-L6-v2` because:

* It’s fast, lightweight, and optimized for semantic similarity
* Strong zero-shot performance across domains
* Works well with FAISS indexing due to embedding dimensionality

### Indexing with FAISS

* Generated embeddings for all text chunks (175K+ total)
* Used FAISS to build a vector index for similarity search
* Stored metadata (product, complaint ID, chunk index) with each vector
* Saved index to: `vector_store/faiss_index.index`

---

## Challenges and Solutions

| Challenge                         | Solution                                      |
| --------------------------------- | --------------------------------------------- |
| Long processing time              | Batched embeddings and used tqdm for tracking |
| Git push failed (large files)     | Added `.gitignore`, considered using DVC      |
| High variance in narrative length | Applied recursive chunking with overlap       |

---

## Next Steps

1. Integrate with LLMs (OpenAI or HuggingFace) using LangChain’s RAG pipeline
2. Enable natural language querying ("Why are users frustrated with BNPL?")
3. Add UI layer using Streamlit or Gradio for non-technical teams
4. Version data and index files with DVC for cleaner Git workflow

---

## Repository Overview

| File / Directory                   | Purpose                                     |
| ---------------------------------- | ------------------------------------------- |
| data/filtered\_complaints.csv      | Cleaned narrative dataset                   |
| vector\_store/faiss\_index.index   | FAISS vector store for retrieval            |
| src/embedding\_indexer.py          | Script for chunking and indexing            |
| notebooks/eda\_preprocessing.ipynb | EDA and cleaning notebook                   |
| requirements.txt                   | Dependencies used in the pipeline           |
| .gitignore                         | To exclude large files from version control |

---

## Conclusion

In one week, we transformed unstructured, noisy customer complaint data into a searchable, semantically rich dataset, indexed using modern vector stores. This foundation enables the next phase: an intelligent assistant that delivers fast, grounded answers to product, support, and compliance teams.

This is more than a pipeline—it’s the beginning of a feedback intelligence engine for fintech at scale.

---