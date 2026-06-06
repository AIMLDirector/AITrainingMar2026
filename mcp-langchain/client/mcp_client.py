import httpx
import os

class MCPClient:
    def __init__(self):
        self.base_url = os.getenv("MCP_BASE_URL")

    async def call_tool(self, tool_name: str, payload: dict):
        async with httpx.AsyncClient() as client:
            res = await client.post(
                f"{self.base_url}/tools/{tool_name}",
                json=payload,
                timeout=30
            )
            res.raise_for_status()
            return res.json()