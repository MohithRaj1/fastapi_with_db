from fastapi import APIRouter

router = APIRouter()

@router.post("/user")
def signup():
    return {"message": "User signed up sucessfully"}

@router.post("/user")
def login():
    return {"message": "User logged in sucessfully"}