

````markdown
# 🧠 CrediTrust Complaint Intelligence – RAG-Powered Q&A System

This project was developed as part of the **10 Academy Week 6 Challenge** to help **CrediTrust Financial** extract insights from unstructured customer complaint narratives using **Retrieval-Augmented Generation (RAG)**.

The solution enables internal teams—like Product, Support, and Compliance—to ask natural language questions and receive synthesized, evidence-backed answers based on real customer complaints.

---

## 📌 Project Objective

Build a production-ready RAG pipeline that:

- Converts raw complaint text into structured semantic chunks
- Embeds and indexes these for fast similarity search
- Generates answers using retrieved evidence and an LLM
- Is accessible via an interactive user interface (Streamlit)

---

## 🗂️ Project Structure

```bash
finance-complaint-insights/
├── data/
│   └── filtered_complaints.csv       # Cleaned complaint narratives
├── vector_store/
│   ├── faiss_index.index             # FAISS vector index
│   └── chunk_metadata.pkl            # Metadata per chunk
├── notebooks/
│   └── eda_preprocessing.ipynb       # Data exploration & cleaning
├── src/
│   ├── embedding_indexer.py          # Chunk + embed pipeline
│   └── rag_pipeline.py               # Core RAG logic
├── app.py                            # Streamlit UI app
├── requirements.txt                  # Python dependencies
└── README.md                         # Project overview (this file)
````

---

## ⚙️ How It Works

### 1. **Data Preprocessing**

* Source: [CFPB Public Complaint Dataset](https://www.consumerfinance.gov/data-research/consumer-complaints/)
* Filtered to 5 product types: Credit Card, BNPL, Personal Loan, Savings, Money Transfer
* Removed empty narratives and cleaned text

### 2. **Chunking & Embedding**

* Used LangChain’s `RecursiveCharacterTextSplitter`
* Embedding model: `all-MiniLM-L6-v2` from SentenceTransformers
* Indexed chunks with FAISS for semantic retrieval

### 3. **RAG Pipeline**

* Retrieves top-k similar chunks from vector store
* Injects them into an LLM prompt
* Generates an answer using Hugging Face `gpt2` (or pluggable with others)

### 4. **User Interface**

* Built with **Streamlit**
* User can type questions and get real-time answers with supporting sources

---

## 🧪 Sample Use Cases

| Question                                      | Example Answer                                  |
| --------------------------------------------- | ----------------------------------------------- |
| Why are customers unhappy with BNPL?          | Customers report refund delays and hidden fees. |
| What are the common issues with Credit Cards? | Credit limit changes and unauthorized charges.  |

---

## 🚀 Run the App Locally

### 1. Clone the repository

```bash
git clone https://github.com/anaol216/finance-complaint-insights.git
cd finance-complaint-insights
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the Streamlit app

```bash
streamlit run app.py
```

---

## 📊 Evaluation & Metrics

| Metric            | Result                                      |
| ----------------- | ------------------------------------------- |
| Chunks Embedded   | 170,000+                                    |
| Retrieval Quality | Top-k semantic matching                     |
| LLM               | GPT-2 (can switch to OpenAI, Mistral, etc.) |
| UI Feedback       | Real-time, transparent, user-friendly       |

---

## ✅ Recommendations for Production

* Replace GPT-2 with instruction-tuned LLM (e.g., LLaMA-3, Mixtral)
* Use OpenAI or HuggingFace APIs for better accuracy
* Add filters by date, product, or company
* Deploy with Streamlit Cloud, Hugging Face Spaces, or Docker

---

## 🧠 Author

**Anaol Atinafu**
AI Fellow, 10 Academy
📧 [atinafuanaol@gmail.com](mailto:atinafuanaol@gmail.com)

---

## 📄 License

This project is for educational and demonstration purposes only.

---

## 🌐 Acknowledgments

* [10 Academy](https://www.10academy.org/)
* [LangChain](https://www.langchain.com/)
* [Sentence Transformers](https://www.sbert.net/)
* [FAISS by Facebook](https://github.com/facebookresearch/faiss)
* [CFPB Data](https://www.consumerfinance.gov/data-research/consumer-complaints/)

```
