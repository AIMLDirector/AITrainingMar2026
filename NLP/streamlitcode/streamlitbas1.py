import streamlit as st 

st.title("AI enabled search engine")
st.write("This is a simple search engine built using Streamlit and Langchain. It uses a local document search tool, Tavily search tool, and DuckDuckGo search tool to provide relevant results to the user.")

st.checkbox("Enable Local Document Search", value=True)
st.checkbox("Enable Tavily Search", value=True)
st.radio("Select Search Tool", options=["Local Document Search", "Tavily Search", "DuckDuckGo Search"], index=0)
st.multiselect("Select Search Tools", options=["Local Document Search", "Tavily Search", "DuckDuckGo Search"], default=["Local Document Search", "Tavily Search"])  
st.slider("Number of Results", min_value=1, max_value=10, value=5)


with st.sidebar:
    st.header("LLM Parameters")
    # API key check
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    
    # Parameters
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    top_k = st.slider("Top-K", 1, 100, 50, 1)
    top_p = st.slider("Top-P", 0.0, 1.0, 0.9, 0.05)