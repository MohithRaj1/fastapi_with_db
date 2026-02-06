from fastapi import FastAPI
from routes.user_route import router as user_router
from db import get_db
app = FastAPI()

app.include_router(user_router)
#to create database

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000)