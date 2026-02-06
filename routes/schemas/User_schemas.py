from db import BaseModel

class UserSchema(BaseModel):
    email: str
    password: str
