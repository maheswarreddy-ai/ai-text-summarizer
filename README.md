# AI Text Summarizer

AI Text Summarizer is a simple NLP application I built to generate concise summaries from long-form text using a pretrained Transformer model.

The application uses **Hugging Face Transformers**, **BART (`facebook/bart-large-cnn`)**, **PyTorch**, and **Streamlit**. The main goal of this project was not only to build a working summarizer, but also to understand how pretrained NLP models can be integrated into a real application.

## Problem Statement

Reading lengthy articles, reports, notes, and documents can be time-consuming. The idea behind this project is to reduce that effort by allowing users to provide text and receive a shorter version containing the most important information.

## Features

* Accepts user-provided text
* Generates abstractive summaries
* Uses the pretrained BART Large CNN model
* Simple web interface built with Streamlit
* Basic input validation
* Runs locally using PyTorch
* Uses an isolated Python virtual environment for dependency management

## Tech Stack

| Technology                | Purpose                                           |
| ------------------------- | ------------------------------------------------- |
| Python                    | Core application development                      |
| Hugging Face Transformers | Loading and working with the pretrained NLP model |
| BART Large CNN            | Text summarization model                          |
| PyTorch                   | Model inference                                   |
| Streamlit                 | Web interface                                     |
| Git & GitHub              | Version control and project hosting               |

## Architecture

```text
User
  │
  ▼
Streamlit UI
  │
  ▼
Input Validation
  │
  ▼
summarize_text()
  │
  ▼
Hugging Face Pipeline
  │
  ▼
Tokenizer
  │
  ▼
BART Large CNN
  │
  ▼
Generated Summary
  │
  ▼
Streamlit UI
```

## How It Works

When the user enters text in the Streamlit application and clicks **Summarize**, the input is passed to the `summarize_text()` function.

The application uses the Hugging Face summarization pipeline with the `facebook/bart-large-cnn` model.

Internally, the input text is tokenized and passed to BART. The model generates a shorter sequence of tokens representing the important information from the original text. These tokens are decoded back into readable text and returned to the Streamlit interface.

The current generation configuration uses:

* `max_length` to limit the maximum summary length
* `min_length` to avoid extremely short summaries
* `do_sample=False` to keep generation deterministic rather than introducing random sampling

## Project Structure

```text
ai-text-summarizer/
│
├── app.py
├── summarizer.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .venv/          # Local only, ignored by Git
```

### `app.py`

Handles the Streamlit interface, receives user input, calls the summarization function, and displays the generated summary.

### `summarizer.py`

Contains the core AI logic. It loads the pretrained BART model through Hugging Face Transformers and exposes the `summarize_text()` function.

### `requirements.txt`

Contains the Python dependencies and versions required to reproduce the project environment.

### `.gitignore`

Prevents local development files such as `.venv` and Python cache files from being committed to the repository.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/maheswarreddy-ai/ai-text-summarizer.git
cd ai-text-summarizer
```

### 2. Create a virtual environment

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

### 4. Run the application

```bash
streamlit run app.py
```

Streamlit will start the application locally in the browser.

## Model

The project uses **`facebook/bart-large-cnn`**, a pretrained sequence-to-sequence Transformer model fine-tuned for abstractive text summarization.

Unlike extractive summarization, which mainly selects sentences from the original text, abstractive summarization can generate new sentences that capture the important meaning of the source content.

## Current Limitations

The current version is intentionally kept simple while I build and understand the core summarization pipeline.

Some current limitations are:

* Very long documents can exceed the model's input token limit.
* Inference can be slow when running BART Large entirely on CPU.
* Only text input is currently supported.
* Summary length uses fixed generation parameters.
* The model is loaded locally, which requires additional memory and storage.

## Planned Improvements

I plan to extend the project with:

* Long-document chunking
* Short, Medium, and Long summary options
* PDF and DOCX support
* Word and token statistics
* Better exception handling
* Loading/progress indicators
* Improved Streamlit interface
* REST API using FastAPI
* Cloud deployment

## What I Learned

Building this project helped me understand the complete workflow of integrating a pretrained NLP model into an application:

```text
User Input
   ↓
Tokenization
   ↓
Transformer Model
   ↓
Text Generation
   ↓
Decoded Summary
   ↓
Application Output
```

I also gained hands-on experience with Python virtual environments, dependency management, Hugging Face Transformers, PyTorch inference, Streamlit, Git, GitHub, and handling library-version compatibility issues.

## Author

**Maheswar Reddy**

AI/ML and Generative AI enthusiast focused on building practical AI applications.

GitHub: `maheswarreddy-ai`
