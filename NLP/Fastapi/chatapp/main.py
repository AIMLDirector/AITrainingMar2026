import streamlit as st
import requests

# Configure the Streamlit page layout
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 LangChain & FastAPI Chatbot")

# URL pointing to your FastAPI backend endpoint
BACKEND_URL = "http://127.0.0.1:8000/chat"

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages from history on application rerun
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# React to user input
if user_prompt := st.chat_input("Type your message here..."):
    
    # 1. Display user message in the UI
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    # 2. Add user message to session memory history
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # 3. Send payload to FastAPI backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                payload = {"message": user_prompt}
                response = requests.post(BACKEND_URL, json=payload)
                
                if response.status_code == 200:
                    ai_reply = response.json().get("reply", "No response content received.")
                    st.markdown(ai_reply)
                    
                    # 4. Save backend assistant reply to session memory history
                    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                else:
                    st.error(f"Backend Error: Received status code {response.status_code}")
                    
            except requests.exceptions.ConnectionError:
                st.error("Failed to connect to the FastAPI backend. Is app.py running?")
