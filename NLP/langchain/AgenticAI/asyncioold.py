import asyncio
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# asyncio to avoid runtime error and to run the code in an asynchronous manner

async def openai_chat():

    model =  await ChatOpenAI(
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

    response = await model.invoke(messages)
    print(response.json())


if __name__ == "__main__":
        asyncio.run(openai_chat())