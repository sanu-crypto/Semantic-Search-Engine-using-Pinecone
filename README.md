# 🔍 Semantic Search Engine using Pinecone

A powerful **Semantic Search Web App** built with **Streamlit, Sentence Transformers, and Pinecone Vector Database**.
This application allows users to upload a text dataset and perform intelligent search using AI embeddings.

---

## 🚀 Features

* 🔎 Semantic search (understands meaning, not just keywords)
* 📂 Upload `.txt` dataset
* 🤖 Uses **SentenceTransformer (MiniLM)** for embeddings
* 🧠 Vector search powered by **Pinecone**
* ⚡ Fast and interactive UI with Streamlit
* 🎯 Returns top relevant results with similarity scores

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Embedding Model**: SentenceTransformers (`all-MiniLM-L6-v2`)
* **Vector Database**: Pinecone
* **Language**: Python

---

## 📁 Project Structure

```
semantic-search/
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/semantic-search.git
cd semantic-search
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Setup Pinecone API Key

1. Go to Pinecone website
2. Create a free account
3. Copy your API key
4. Paste it in `app.py`:

```
PINECONE_API_KEY = "your_api_key_here"
```

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 📂 Input File Format

Upload a `.txt` file in this format:

```
What is AI?
Artificial Intelligence is the simulation of human intelligence.

What is Machine Learning?
Machine Learning is a subset of AI that learns from data.
```

---

## 🔍 How It Works

1. Upload text file
2. Text is converted into embeddings using SentenceTransformer
3. Embeddings are stored in Pinecone
4. User enters query
5. Query is converted into embedding
6. Pinecone returns most similar results

---

## 📸 Output Example

* Displays top 3 most relevant results
* Shows similarity score
* Clean UI cards for results

---

## ⚠️ Notes

* A new Pinecone index may be created on each run (for testing)
* For production, use a fixed index name
* Ensure embedding dimension matches index dimension (384)

---

## 🔮 Future Enhancements

* 📄 PDF document search
* 💬 ChatGPT-like Q&A system (RAG)
* 🌐 Deploy on Streamlit Cloud
* 🧠 Multi-file support
* 📊 Dashboard for analytics

---

## 👨‍💻 Author

**Sayan Das**
B.E. AI & Data Science

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🔁 Share with others

---
