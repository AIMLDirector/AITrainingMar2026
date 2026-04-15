from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Initialize the LangChain Azure chat model
model = AzureChatOpenAI(
    azure_endpoint="https://premk-mh8fcwaa-eastus2.cognitiveservices.azure.com/",
    azure_deployment="gpt-4.1-mini",
    api_version="2024-12-01-preview",
    api_key="YOUR_SUBSCRIPTION_KEY",
    temperature=1.0,
    max_tokens=13107
)

# Prepare messages
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="I am going to Paris, what should I see?")
]

# Invoke the model
response = model.invoke(messages)

print(response.content)
