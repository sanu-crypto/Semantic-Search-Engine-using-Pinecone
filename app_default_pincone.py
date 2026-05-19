import streamlit as st
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import numpy as np
import time
import html
import uuid

# ---------------- CONFIG ---------------- #
PINECONE_API_KEY = "pcsk_69sqiG_6aLELqcAF*********************************************gNaHi2BA5"#To get this API we need to go to PINCONE and get the API

# 🔥 UNIQUE INDEX EVERY RUN (NO ERRORS EVER)
INDEX_NAME = f"semantic-search-{uuid.uuid4().hex[:6]}"

DIMENSION = 384
NAMESPACE = "default"

# ---------------- PAGE ---------------- #
st.set_page_config(page_title="Semantic Search", layout="wide")

st.title("🔍 Semantic Search Engine (Pinecone)")
st.write("SentenceTransformer + Pinecone")

# ---------------- MODEL ---------------- #
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts, model):
    return np.array(model.encode(texts)).astype("float32")

# ---------------- LOAD FILE ---------------- #
def load_docs(file):
    content = file.read().decode("utf-8")
    lines = [line.strip() for line in content.splitlines() if line.strip()]

    docs = [
        f"{lines[i]} {lines[i+1]}"
        for i in range(0, len(lines)-1, 2)
    ]
    return docs

# ---------------- PINECONE ---------------- #
@st.cache_resource
def init_pinecone(index_name):
    pc = Pinecone(api_key=PINECONE_API_KEY)

    pc.create_index(
        name=index_name,
        dimension=DIMENSION,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

    # wait for ready
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

    return pc.Index(index_name)

# ---------------- UPLOAD ---------------- #
def upload(index, docs, model):
    embeddings = embed(docs, model)

    vectors = []
    for i, doc in enumerate(docs):
        vectors.append({
            "id": f"id-{i}",
            "values": embeddings[i].tolist(),
            "metadata": {"text": doc}
        })

    index.upsert(vectors=vectors, namespace=NAMESPACE)

# ---------------- SEARCH ---------------- #
def search(query, model, index):
    q = embed([query], model)[0].tolist()

    res = index.query(
        vector=q,
        top_k=3,
        include_metadata=True,
        namespace=NAMESPACE
    )

    return [(m["metadata"]["text"], m["score"]) for m in res["matches"]]

# ---------------- UI ---------------- #
uploaded = st.file_uploader("Upload .txt file", type=["txt"])
query = st.text_input("Enter your question")

if uploaded:

    docs = load_docs(uploaded)
    st.success(f"{len(docs)} documents loaded")

    model = load_model()

    with st.spinner("Creating Pinecone index..."):
        index = init_pinecone(INDEX_NAME)

    with st.spinner("Uploading data..."):
        upload(index, docs, model)

    st.success("Data uploaded successfully")

    if query:
        results = search(query, model, index)

        st.subheader("Results")

        for doc, score in results:
            st.markdown(f"""
            <div style="background:#1e293b;padding:15px;border-radius:10px;margin-bottom:10px">
                <b>Score:</b> {score:.4f}<br><br>
                {html.escape(doc)}
            </div>
            """, unsafe_allow_html=True)
