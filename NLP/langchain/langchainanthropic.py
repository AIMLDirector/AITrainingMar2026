from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(
    model="claude-sonnet-4-5-20250929",
    temperature=0.7,
    max_tokens=600,
    max_retries=2
)

messages = [
    HumanMessage(content="Hello, how are you?")
]

# Invoke the model
response = model.invoke(messages)

print(response.content)