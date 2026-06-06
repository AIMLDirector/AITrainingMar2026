import os
import requests
from datetime import datetime
from zoneinfo import ZoneInfo
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from google.adk.agents.llm_agent import Agent

# -------------------------------
# 🌍 Setup for Timezone Detection
# -------------------------------
geolocator = Nominatim(user_agent="ai_interviewer_agent")
tf = TimezoneFinder()


# -------------------------------
# 🔎 Tool 1: Live Web Search
# -------------------------------
def search_live_data(query: str) -> str:
    """
    Searches the live web using Serper API.
    """
    url = "https://google.serper.dev/search"

    api_key = os.environ.get("SERP_API_KEY")
    if not api_key:
        return "Serper API key is missing."

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "q": query,
        "num": 5
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        results = []
        for item in data.get("organic", [])[:3]:
            title = item.get("title", "")
            snippet = item.get("snippet", "")
            link = item.get("link", "")

            results.append(f"{title}\n{snippet}\n{link}\n")

        return "\n".join(results) if results else "No results found."

    except Exception as e:
        return f"Search failed: {str(e)}"


# -------------------------------
# 🕒 Tool 2: Dynamic Time by City
# -------------------------------
def get_current_time(city: str) -> str:
    """
    Returns real-time current time based on any city globally.
    """
    try:
        location = geolocator.geocode(city)

        if not location:
            return f"Could not find location: {city}"

        timezone_str = tf.timezone_at(
            lng=location.longitude,
            lat=location.latitude
        )

        if not timezone_str:
            return f"Could not determine timezone for {city}"

        now = datetime.now(ZoneInfo(timezone_str))

        formatted_time = now.strftime("%I:%M %p, %d %B %Y")

        return f"Current time in {city.title()} is {formatted_time}"

    except Exception as e:
        return f"Error fetching time: {str(e)}"


# -------------------------------
# 🤖 AI Agent Configuration
# -------------------------------
root_agent = Agent(
    model='gemini-2.5-flash',
    name='interviewer_agent',
    description='AI assistant with real-time search and global time capability.',
    instruction="""
    You are a smart AI assistant.

    - Use search_live_data for latest or real-time information.
    - Use get_current_time when user asks about time in any city.
    - Always respond in a clean, human-readable format.
    - Keep answers concise and helpful.
    """,
    tools=[search_live_data, get_current_time]
)


# -------------------------------
# 🧪 Example Run (for testing)
# -------------------------------
if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        response = root_agent.run(user_input)
        print("AI:", response)
