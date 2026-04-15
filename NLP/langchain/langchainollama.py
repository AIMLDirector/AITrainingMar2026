from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

model = ChatOllama(
    model="qwen3.5:2b",
    temperature=0.7,
    max_tokens=600,
    max_retries=2
)

prompt_input = input("Enter user prompt input: ")

messages = [
    SystemMessage(content="You are a helpful assistant of Data engineering team and SME . provide clear and concise answers to user queries related to data engineering topics."),
    HumanMessage(content=prompt_input),
   
]

response = model.invoke(messages)   
print(response.content)
