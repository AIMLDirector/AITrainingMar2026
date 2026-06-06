from pydantic import BaseModel

class CandidateQuery(BaseModel):
    skill: str
    min_score: int = 70