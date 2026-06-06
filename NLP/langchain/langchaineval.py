from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# Main Model
# -----------------------------
model = init_chat_model(
    "gpt-5-nano",
    temperature=0.7,
    max_tokens=600,
    max_retries=2
)

# -----------------------------
# Rogue / Relevance Scorer Model
# -----------------------------
scorer_model = init_chat_model(
    "gpt-4.1-mini",
    temperature=0
)

# -----------------------------
# System Prompt
# -----------------------------
system_msg = SystemMessage(content="""
You are a senior Python developer with expertise in web frameworks.
Always provide code examples and explain your reasoning.
Be concise but thorough in your explanations.
""")

# -----------------------------
# User Input
# -----------------------------
user_input = input("What do you want to ask the Python expert? ")

messages = [
    system_msg,
    HumanMessage(content=user_input)
]

# -----------------------------
# Generate Response
# -----------------------------
response = model.invoke(messages)

print("\n================ AI RESPONSE ================\n")
print(response.content)

# -----------------------------
# Rogue / Quality Scorer Prompt
# -----------------------------
scorer_prompt = f"""
You are an AI response evaluator.

Evaluate the following AI response based on:

1. Relevance to the user's question
2. Technical correctness
3. Clarity
4. Hallucination risk
5. Completeness

User Question:
{user_input}

AI Response:
{response.content}

Return output in this format:

Score: <1-10>

Strengths:
- item 1
- item 2

Weaknesses:
- item 1
- item 2

Hallucination Risk:
Low / Medium / High

Final Verdict:
<short summary>
"""

# -----------------------------
# Evaluate Response
# -----------------------------
score_response = scorer_model.invoke([
    HumanMessage(content=scorer_prompt)
])

print("\n================ ROGUE SCORER ================\n")
print(score_response.content)