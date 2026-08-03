from dotenv import load_dotenv

# import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models import incident, log  # important import  # noqa: F401
from app.routers import analysis, copilot, health, upload

load_dotenv()

# print("API KEY:", os.getenv("OPENAI_API_KEY"))  # keep for debug

app = FastAPI(title="AI Log Intelligence API")


# app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(health.router)
app.include_router(upload.router)
app.include_router(analysis.router)
app.include_router(copilot.router)