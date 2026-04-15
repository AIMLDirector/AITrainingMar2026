from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.agents.middleware import PIIMiddleware
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


# Initialize the LangChain OpenAI chat model
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7,
    max_tokens=600,
    max_retries=2
)

# PII_filter = PIIMiddleware(
#     pii_types=["email","credit_card"],
#     strategy="mask"
# )

agent = create_agent(
            model=llm,
            system_prompt="You are a helpful assistant of Data engineering team and SME . provide clear and concise answers to user queries related to data engineering topics.",
            tools=[],
            middleware=[
        PIIMiddleware("email", strategy="redact", apply_to_input=True),
        PIIMiddleware("credit_card", strategy="mask", apply_to_input=True),
    ],
)


user_input = input("Enter your query: ")

response = agent.invoke({"messages": [{"role": "user", "content":user_input}]})


print(response["messages"][-1].content)