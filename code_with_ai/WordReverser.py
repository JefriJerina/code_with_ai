# WordReverser.py

import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the model only once
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# Initialize memory in session state
if "memory" not in st.session_state:
    st.session_state.memory = []  # list of (embedding, input, output)

def embed_text(text):
    return model.encode([text])[0]

def retrieve_or_generate(sentence, threshold=0.9):
    query_vector = embed_text(sentence)
    for stored_vector, stored_input, stored_output in st.session_state.memory:
        score = cosine_similarity([query_vector], [stored_vector])[0][0]
        if score >= threshold:
            return stored_output, "📦 Retrieved from self memory"
    
    # If not found
    result = ' '.join(word[::-1] for word in sentence.split())
    st.session_state.memory.append((query_vector, sentence, result))
    return result, "🧠 Newly computed"

# UI with Streamlit
st.title("🔁 Word Reverser (Self RAG-powered)")
st.markdown("Reverse each word in a sentence. Cached using self-memory (RAG style).")

user_input = st.text_input("Enter a sentence:")

if user_input:
    output, status = retrieve_or_generate(user_input)
    st.success(status)
    st.write("🔄 **Reversed Sentence:**", output)

# Optional: Show memory for debug/demo
with st.expander("🧠 View Self RAG Memory"):
    for idx, (_, inp, out) in enumerate(st.session_state.memory):
        st.write(f"{idx+1}. **Input:** {inp} → **Output:** {out}")
