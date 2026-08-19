from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)


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

    result = summarizer(
        text,
        min_length=min_len,
        max_length=max_len,
        do_sample=False
    )

    return result[0]["summary_text"]