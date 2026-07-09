# 🩺 Health Query Chatbot

An NLP-powered chatbot designed to understand and respond to health-related queries. The system leverages **Sentence Transformers** and the **MiniLM** architecture to semantically match user questions with the most relevant medical information, trained on a variety of medical datasets.

## 📖 Overview

Health Query Chatbot is a conversational AI system built to help users get quick, reliable answers to common medical and health-related questions. Instead of relying on simple keyword matching, the chatbot uses **semantic similarity search** powered by transformer-based sentence embeddings — allowing it to understand the *meaning* behind a query rather than just the exact wording.

This makes the chatbot capable of handling paraphrased questions, informal phrasing, and varied sentence structures while still returning accurate, contextually relevant responses.

## ✨ Key Features

- **Semantic Understanding** — Uses sentence embeddings to capture the true intent of user queries, not just keyword overlap
- **Medical Domain Training** — Trained on multiple medical/health-related datasets for domain-specific accuracy
- **Lightweight & Fast** — Built on MiniLM, a compact transformer model that offers strong performance with lower computational cost
- **Similarity-Based Response Matching** — Retrieves the most relevant answer by comparing query embeddings against a knowledge base
- **Scalable Pipeline** — Easy to extend with additional datasets or fine-tune further for specific medical domains

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| NLP Framework | Sentence Transformers (SBERT) |
| Model | MiniLM |
| Core Libraries | Hugging Face Transformers, PyTorch, scikit-learn, pandas, NumPy |

## 🧠 How It Works

1. **Data Preparation** — Medical datasets are cleaned and preprocessed into query-response (or question-answer) pairs
2. **Embedding Generation** — Each query/response is converted into a dense vector representation using the Sentence Transformer (MiniLM) model
3. **Similarity Matching** — When a user asks a question, its embedding is compared against the precomputed embeddings using cosine similarity
4. **Response Retrieval** — The most semantically similar match is returned as the chatbot's response

## 📊 Datasets

The model was trained/fine-tuned using a combination of publicly available medical and health-related datasets, covering topics such as symptoms, conditions, treatments, and general health FAQs.

> *(Add the specific dataset names and sources here, e.g., MedQuAD, iCliniq, HealthTap, etc.)*

## 🚀 Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Installation
```bash
git clone https://github.com/<your-username>/health-query-chatbot.git
cd health-query-chatbot
pip install -r requirements.txt
```

### Usage
```bash
python app.py
```

## 📁 Project Structure
```
health-query-chatbot/
├── data/               # Medical datasets
├── models/             # Trained/fine-tuned model files
├── src/                # Source code (preprocessing, training, inference)
├── app.py              # Main application entry point
├── requirements.txt
└── README.md
```

## ⚠️ Disclaimer

This chatbot is intended for **informational and educational purposes only**. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

## 🔮 Future Improvements

- Expand dataset coverage for broader medical topics
- Add multi-turn conversation support
- Deploy as a web app / API
- Integrate a larger transformer model for improved accuracy

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
