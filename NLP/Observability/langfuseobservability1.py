import os
import uuid
from dotenv import load_dotenv
from openai import OpenAI
from langfuse import observe, Langfuse
from langfuse.openai import openai

load_dotenv()

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@observe(name="dynamic-story-generator")
def generate_story(prompt: str, user_id: str, session_id: str):

    # Add metadata + tags here (NOT in decorator)
    langfuse.trace(
        user_id=user_id,
        session_id=session_id,
        tags=["demo", "llm", "openai"],
        metadata={
            "feature": "story_generation",
            "environment": "dev"
        }
    )

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a creative storyteller."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    return response


if __name__ == "__main__":
    try:
        user_prompt = input("Enter your story topic: ")
        user_id = "kumar"
        session_id = str(uuid.uuid4())

        result = generate_story(user_prompt, user_id, session_id)

        print("\nGenerated Story:\n")
        print(result.choices[0].message.content)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        langfuse.flush()