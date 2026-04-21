import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

# App Title
st.set_page_config(page_title="LangChain Chatbot")
st.title("LangChain Chatbot")

# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.header("LLM Parameters")
   
    # Parameters
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    top_k = st.slider("Top-K", 1, 100, 50, 1)
    top_p = st.slider("Top-P", 0.0, 1.0, 0.9, 0.05)

# --- SESSION STATE MANAGEMENT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- CHAT INTERFACE (Bottom) ---
if prompt := st.chat_input("how can i help you ?"):

        
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- LANGCHAIN INTEGRATION ---
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Initialize Model
            llm = ChatOpenAI(
                temperature=temperature,
                top_p=top_p,
                 max_tokens=600,
                 max_retries=2
                # model_kwargs={"top_k": top_k, "top_p": top_p}
            )
            
            # Format history for LangChain
            chat_history = [
                HumanMessage(content=m["content"]) if m["role"] == "user" 
                else AIMessage(content=m["content"])
                for m in st.session_state.messages
            ]
            
            # Generate response
            response = llm.invoke(chat_history)
            st.markdown(response.content)
            
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response.content})
