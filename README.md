# AI Text Summarizer

AI Text Summarizer is an NLP application I built to generate concise summaries from long-form text using pretrained Transformer models.

The project is built with **Python, Hugging Face Transformers, PyTorch, DistilBART, and Streamlit**. I initially tested `facebook/bart-large-cnn` and later evaluated a distilled BART model to improve inference speed on CPU.

## Problem Statement

Reading long articles, reports, notes, and documents can take a significant amount of time.

The goal of this project is to provide a simple interface where users can paste text and generate a shorter summary containing the important information.

## Features

* Accepts user-provided text
* Generates abstractive summaries
* Supports Short, Medium, and Long summary options
* Displays input word count
* Displays summary word count
* Measures summary generation time
* Handles empty and very short inputs
* Supports long text through chunking
* Runs locally using PyTorch
* Provides an interactive Streamlit interface

## Tech Stack

| Technology                | Purpose                                 |
| ------------------------- | --------------------------------------- |
| Python                    | Core application development            |
| Hugging Face Transformers | Loading and using pretrained NLP models |
| DistilBART                | Current summarization model             |
| PyTorch                   | Model inference                         |
| Streamlit                 | Web interface                           |
| Git                       | Version control                         |
| GitHub                    | Project hosting                         |

## Current Model

The current version uses:

```text
sshleifer/distilbart-cnn-12-6
```

This model is a distilled version of BART designed to provide a better balance between summarization quality and inference speed.

I initially used:

```text
facebook/bart-large-cnn
```

but CPU inference was slower, so I compared it with DistilBART.

## Model Performance Comparison

I tested both models on the same machine using CPU inference.

| Model                         | Summary Words | Generation Time |
| ----------------------------- | ------------: | --------------: |
| facebook/bart-large-cnn       |            41 |         26.15 s |
| sshleifer/distilbart-cnn-12-6 |            44 |         18.76 s |

In this test, DistilBART reduced generation time by approximately 28% while producing a summary of similar length.

Because the application currently runs on CPU, I selected DistilBART for the latest version.

## Project Architecture

```text
User
  |
  v
Streamlit UI
  |
  v
Input Validation
  |
  v
Summary Length Selection
  |
  v
summarize_text()
  |
  v
Check Input Length
  |
  v
Split Long Text into Chunks
  |
  v
DistilBART Summarization Pipeline
  |
  v
Summarize Each Chunk
  |
  v
Combine Chunk Summaries
  |
  v
Display Final Summary
```

## How It Works

The user enters text through the Streamlit interface.

The application first validates the input and calculates the number of words.

The user can select one of three summary lengths:

```text
Short
Medium
Long
```

The selected option controls the minimum and maximum generated summary length.

For long input text, the application splits the text into smaller chunks before sending each chunk to the summarization model.

Each chunk is summarized individually and the results are combined into the final output.

The application also measures how long the summarization process takes.

## Summary Length Options

The current configuration uses:

```text
Short
min_length = 20
max_length = 50

Medium
min_length = 30
max_length = 80

Long
min_length = 50
max_length = 120
```

The generation process uses:

```text
do_sample = False
```

This avoids random sampling and helps produce more consistent summaries.

## Long-Text Handling

Transformer models have maximum input token limits.

To avoid sending very large text directly to the model, the application currently splits long input into smaller word-based chunks.

Example:

```text
1200-word document
       |
       v
500 words
500 words
200 words
       |
       v
Summarize each chunk
       |
       v
Combine summaries
```

This is the first version of long-document handling.

A future improvement will replace word-based chunking with token-based chunking because Transformer limits are based on tokens rather than words.

## Project Structure

```text
ai-text-summarizer/
|
|-- app.py
|-- summarizer.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|
`-- .venv/        # Local environment, ignored by Git
```

### `app.py`

Handles:

* Streamlit UI
* Text input
* Input word count
* Summary-length selection
* Loading spinner
* Summary output
* Summary word count
* Generation-time measurement

### `summarizer.py`

Handles:

* Loading the Transformer summarization pipeline
* Loading DistilBART
* Input validation
* Summary-length configuration
* Long-text chunking
* Summarizing each chunk
* Returning the final summary

### `requirements.txt`

Contains the Python packages and versions required to reproduce the project environment.

### `.gitignore`

Prevents unnecessary development files such as `.venv` and Python cache files from being uploaded to GitHub.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/maheswarreddy-ai/ai-text-summarizer.git
cd ai-text-summarizer
```

### 2. Create a Python virtual environment

```bash
py -3.11 -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in the browser.

The default local address is usually:

```text
http://localhost:8501
```

## Current Limitations

* Chunking is currently based on words instead of tokenizer tokens
* Each chunk requires a separate model inference call
* Long documents therefore take more time to summarize
* CPU inference is slower than GPU inference
* PDF and DOCX files are not yet supported
* Combined chunk summaries are not currently re-summarized

## Planned Improvements

* Token-based chunking
* Final re-summarization of chunk summaries
* PDF upload
* DOCX upload
* Better UI design
* Model selection from the interface
* More systematic model benchmarking
* Improved exception handling
* Caching
* FastAPI backend
* Cloud deployment

## What I Learned

This project helped me understand the complete workflow of integrating a pretrained NLP model into an application:

```text
User Input
   |
   v
Validation
   |
   v
Chunking
   |
   v
Tokenization
   |
   v
Transformer Model
   |
   v
Generated Summary
   |
   v
Application Output
```

I also gained hands-on experience with:

* Python virtual environments
* Dependency management
* Hugging Face Transformers
* BART and DistilBART
* PyTorch inference
* Streamlit
* Model latency measurement
* Model comparison
* Long-text handling
* Git
* GitHub
* Library-version compatibility

## Author

**Maheswar Reddy**

Building practical AI/ML and Generative AI applications.

GitHub: `maheswarreddy-ai`
