from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="MCP Server")

# -------------------------
# Schemas
# -------------------------
class CandidateQuery(BaseModel):
    skill: str
    min_score: int = 70

class Candidate(BaseModel):
    name: str
    skill: str
    score: int

# -------------------------
# Mock DB
# -------------------------
DB = [
    {"name": "Arun", "skill": "Python", "score": 92},
    {"name": "Priya", "skill": "AI", "score": 89},
    {"name": "Rahul", "skill": "Java", "score": 75},
    {"name": "Sneha", "skill": "Python", "score": 85},
]

# -------------------------
# Tools
# -------------------------
@app.post("/tools/search_candidates")
async def search_candidates(query: CandidateQuery):
    results = [
        c for c in DB
        if query.skill.lower() in c["skill"].lower()
        and c["score"] >= query.min_score
    ]
    return {"results": results}


@app.post("/tools/evaluate_candidate")
async def evaluate_candidate(data: dict):
    name = data.get("name", "Unknown")

    return {
        "candidate": name,
        "technical_score": 85,
        "soft_skill_score": 80,
        "overall": 83,
        "recommendation": "Hire"
    }