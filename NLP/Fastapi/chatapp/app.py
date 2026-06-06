import os
from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load API keys from .env file
load_dotenv()

app = FastAPI(title="AI Chatbot Backend")

# Initialize the LLM once globally
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7  # Higher temperature for more conversational responses
)

# Define the expected JSON structure from the frontend
class ChatRequest(BaseModel):
    message: str = Field(..., description="The user message sent to the chatbot.")

@app.post("/chat")
async def handle_chat(payload: ChatRequest):
    # Pass user message to LangChain ChatOpenAI model
    response = await llm.ainvoke([HumanMessage(content=payload.message)])
    
    # Return JSON response back to Streamlit
    return {"reply": response.content}
