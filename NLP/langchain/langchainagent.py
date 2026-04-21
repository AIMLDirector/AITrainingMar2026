from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()


model = init_chat_model("gpt-5-nano",  temperature=0.7, max_tokens=600, max_retries=2)

system_msg = SystemMessage("""
You are a senior Python developer with expertise in web frameworks.
Always provide code examples and explain your reasoning.
Be concise but thorough in your explanations.
""")

user_input = input("What do you want to ask the Python expert? ")
messages = [system_msg, HumanMessage(content=user_input)]

response = model.invoke(messages)
print(response.content)