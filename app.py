import streamlit as st
from src.rag_pipeline import rag_answer

# Page configuration
st.set_page_config(page_title="CrediTrust AI Assistant", layout="wide")

# Title and description
st.title("CrediTrust Financial Complaint Assistant")
st.markdown("Ask a question based on customer complaint data from financial products like credit cards, loans, and more.")

# Input box
query = st.text_area("### Enter your question:", placeholder="e.g., What are the most common issues with Buy Now Pay Later?", height=100)

# Buttons
col1, col2 = st.columns([1, 1])
submit_clicked = col1.button("Ask")
clear_clicked = col2.button("Clear")

# Session state for clearing
if clear_clicked:
    st.rerun()  

# Answer display
if submit_clicked:
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Thinking... Please wait."):
            result = rag_answer(query)

        st.markdown("### Answer")
        st.success(result["answer"])

        st.markdown("---")
        st.markdown("### Retrieved Source Chunks")
        for i, src in enumerate(result["sources"][:3], 1):
            st.markdown(f"**[{i}] Product:** {src.get('product', 'N/A')}")
            st.markdown(f"**Complaint ID:** {src.get('complaint_id', 'N/A')}")
            st.code(src.get("text", "No preview available...")[:500], language="text")

