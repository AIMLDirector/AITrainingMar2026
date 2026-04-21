from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool, ToolRuntime
from dotenv import load_dotenv
load_dotenv()

# Initialize the LangChain OpenAI chat model
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7,
    max_tokens=600,
    max_retries=2
)

@tool
def get_current_time() -> str:
    """Get the current time."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")



# Create an agent with the specified LLM    
agent = create_agent(
            model=llm,
            system_prompt="You are a helpful assistant of Data engineering team and SME . provide clear and concise answers to user queries related to data engineering topics.",
            tools=[get_current_time],
)

# Get user input
user_input = input("Enter your query: ")

# Invoke the agent with the user input
response = agent.invoke({"messages": [{"role": "user", "content":user_input}]})


print(response["messages"][-1].content)