from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)


def split_text(text, max_words=500):
    words = text.split()

    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks


def summarize_text(text, summary_length="Medium"):
    if not text.strip():
        return "Please enter some text."

    if summary_length == "Short":
        min_len = 20
        max_len = 50

    elif summary_length == "Medium":
        min_len = 30
        max_len = 80

    else:
        min_len = 50
        max_len = 120

    chunks = split_text(text)

    summaries = []

    for chunk in chunks:
        result = summarizer(
            chunk,
            min_length=min_len,
            max_length=max_len,
            do_sample=False
        )

        summaries.append(result[0]["summary_text"])

    final_summary = " ".join(summaries)

    return final_summary