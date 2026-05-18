from pydantic import BaseModel

class AIResponse(BaseModel):
    topic : str
    difficulty : str
    answer : str