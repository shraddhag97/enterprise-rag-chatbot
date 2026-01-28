import streamlit as st
import requests
import uuid

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="Enterprise RAG Chatbot", page_icon="🤖")

st.title("Enterprise RAG Chatbot")

# Create a session_id once per browser session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Store chat history for UI rendering
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask something about the documents...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    payload = {
        "session_id": st.session_state.session_id,
        "message": user_input
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=30)
        response.raise_for_status()
        answer = response.json()["answer"]
    except Exception as e:
        answer = f"Error: {e}"

    # Show bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
    with st.chat_message("assistant"):
        st.markdown(answer)
