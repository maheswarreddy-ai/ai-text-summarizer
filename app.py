import time
import streamlit as st

from summarizer import summarize_text


st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="centered"
)

st.title("📝 AI Text Summarizer")

st.write(
    "Paste long text below and generate a concise AI-powered summary."
)

text = st.text_area(
    "Enter text to summarize",
    height=300,
    placeholder="Paste your article, notes, report, or long document here..."
)

word_count = len(text.split())

st.caption(f"Input word count: {word_count}")

summary_length = st.selectbox(
    "Choose summary length",
    ["Short", "Medium", "Long"]
)

if st.button("Summarize", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text.")

    elif word_count < 30:
        st.warning("Please enter at least 30 words for a meaningful summary.")

    else:
        with st.spinner("Generating summary..."):
            start_time = time.time()

            summary = summarize_text(
                text,
                summary_length
            )

            end_time = time.time()

        summary_word_count = len(summary.split())

        st.success("Summary generated successfully!")

        st.subheader("Summary")

        st.write(summary)

        st.caption(
            f"Input words: {word_count} | "
            f"Summary words: {summary_word_count} | "
            f"Generated in {end_time - start_time:.2f} seconds"
        )