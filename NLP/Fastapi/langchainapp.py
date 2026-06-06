import os
from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
load_dotenv()

app = FastAPI(title="LangChain AI Service")

llm = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature=0,       
)

class TextPayload(BaseModel):
    text: str = Field(..., min_length=3, description="The content to analyze.")
    max_length: int = Field(512, description="Maximum token length for output.")


@app.post("/predict-sentiment")
async def predict_sentiment(payload: TextPayload):
    

    prompt = f"Analyze the sentiment of this text. Respond with only one word (Positive, Negative, or Neutral): {payload.text}"
    
    response = await llm.ainvoke([HumanMessage(content=prompt)])
    sentiment_result = response.content.strip()
    
    return {
        "processed_text": payload.text,
        "sentiment": sentiment_result,
        "max_length_configured": payload.max_length
    }
