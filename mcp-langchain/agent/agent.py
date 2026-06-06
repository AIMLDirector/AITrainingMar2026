import sys
import os
from dotenv import load_dotenv

# -------------------------
# Load ENV
# -------------------------
load_dotenv()

# -------------------------
# Fix Import Path
# -------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# -------------------------
# Imports
# -------------------------
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from client.mcp_tool import TOOLS

# -------------------------
# Initialize LLM
# -------------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# -------------------------
# Create Agent
# -------------------------
agent = create_agent(
    model=llm,
    tools=TOOLS,
    system_prompt="""
You are an AI HR assistant.

Your responsibilities:
1. Search candidates based on skill and score
2. Evaluate shortlisted candidates
3. Provide clear hiring recommendations

Always:
- First search candidates
- Then evaluate each candidate
- Return structured insights
"""
)

# -------------------------
# Run Agent
# -------------------------
if __name__ == "__main__":
    try:
        query = "Find Python candidates above score 80 and evaluate them"

        response = agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        })

        def _extract_final_output(resp):
            if isinstance(resp, dict):
                messages = resp.get("messages")
                if isinstance(messages, list) and messages:
                    last = messages[-1]
                    if hasattr(last, "content"):
                        return last.content
                    if isinstance(last, dict):
                        return last.get("content") or str(last)
                    return str(last)
                if resp.get("output"):
                    return resp["output"]
            return str(resp)

        final_output = _extract_final_output(response)

        print(final_output)

    except Exception as e:
        print(f"\n❌ Error: {e}")