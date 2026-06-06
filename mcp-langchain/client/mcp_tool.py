import asyncio
from langchain.tools import tool
from client.mcp_client import MCPClient

# -------------------------
# MCP Client Instance
# -------------------------
client = MCPClient()


# -------------------------
# Helper: Run async safely
# -------------------------
def run_async(coro):
    try:
        return asyncio.run(coro)
    except RuntimeError:
        # Fix for "event loop already running"
        import nest_asyncio
        nest_asyncio.apply()
        return asyncio.get_event_loop().run_until_complete(coro)


# -------------------------
# Tool 1: Search Candidates
# -------------------------
@tool
def search_candidates(skill: str, min_score: int) -> dict:

    """
        Search candidates by skill and minimum score.

        Args:
            skill (str): Skill to filter (e.g., Python, AI)
            min_score (int): Minimum score threshold

        Returns:
            dict: List of matching candidates
    """
    payload = {
        "skill": skill,
        "min_score": min_score
    }

    return run_async(
        client.call_tool("search_candidates", payload)
    )
    

# -------------------------
# Tool 2: Evaluate Candidate
# -------------------------
@tool
def evaluate_candidate(name: str) -> dict:
    '''
    Evaluate a candidate and return hiring recommendation.

    Args:
        name (str): Candidate name

    Returns:
        dict: Evaluation result with scores and recommendation
    '''
    payload = {
        "name": name
    }

    return run_async(
        client.call_tool("evaluate_candidate", payload)
    )


# -------------------------
# Export Tools
# -------------------------


TOOLS = [
    search_candidates,
    evaluate_candidate
]