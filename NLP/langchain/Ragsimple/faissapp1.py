import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS


load_dotenv()

VECTOR_DB_PATH = "faiss_warpstream_db"

embeddings = OpenAIEmbeddings()
db = FAISS.load_local(VECTOR_DB_PATH, embeddings, allow_dangerous_deserialization=True)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

st.set_page_config(page_title="Data Engineering Copilot", layout="wide")
st.title("Data Engineering Copilot")


if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about Kafka, WarpStream, pipelines..."):

    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

   
    with st.spinner("Searching knowledge base..."):
        docs = db.similarity_search(prompt, k=3)

    context = "\n\n".join([d.page_content for d in docs])

   
    full_prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {prompt}
    """

    with st.chat_message("assistant"):
        response = llm.invoke(full_prompt)
        st.markdown(response.content)

   
    st.session_state.messages.append(
        {"role": "assistant", "content": response.content}
    )