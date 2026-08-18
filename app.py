import streamlit as st
from summarizer import summarize_text

st.title("AI Text Summarizer")

text = st.text_area(
    "Enter text to summarize",
    height=250
)

if st.button("Summarize"):
    if text.strip():
        summary = summarize_text(text)

        st.subheader("Summary")
        st.write(summary)
    else:
        st.warning("Please enter some text.")