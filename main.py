import os
import sys

# Ensure the project root is in the Python path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR) # Use insert(0) to prioritize

print(f"CWD: {os.getcwd()}")
print(f"ROOT_DIR: {ROOT_DIR}")
print(f"sys.path: {sys.path}")
try:
    print(f"Files in root: {os.listdir(ROOT_DIR)}")
    print(f"Files in schemas/: {os.listdir(os.path.join(ROOT_DIR, 'schemas'))}")
except Exception as e:
    print(f"Diagnostic error: {e}")

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.ai_response_routes import router as ai_response_router
from routes.email_routes import router as email_router
from sqlalchemy import create_engine
import os
from models import Base
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(ai_response_router)
app.include_router(email_router)

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
