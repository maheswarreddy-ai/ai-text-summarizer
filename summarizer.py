from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


def summarize_text(text):
    if not text.strip():
        return "Please enter some text."

    result = summarizer(
        text,
        max_length=80,
        min_length=25,
        do_sample=False
    )

    return result[0]["summary_text"]


text = input("Enter text to summarize: ")

summary = summarize_text(text)

print("\nSummary:")
print(summary)