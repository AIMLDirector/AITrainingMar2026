from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()


model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.6,
    max_tokens=500,
    max_retries=2,
)

messages = [
    (
        "system",
        "You are a helpful translator. Translate the user sentence to French.",
    ),
    ("human", "I love programming."),
]

response = model.invoke(messages)
print(response.json())