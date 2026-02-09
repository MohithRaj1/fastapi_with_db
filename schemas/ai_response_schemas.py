from pydantic import BaseModel


class AIRequest(BaseModel):
    message: str
    system_prompt:str="you are helpfull assistant"

class AIResponse(BaseModel):
    response: str
