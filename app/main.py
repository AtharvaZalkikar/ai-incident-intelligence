from dotenv import load_dotenv
# import os

from fastapi import FastAPI
from app.routers import health, upload, analysis
from app.database import engine, Base
from app.models import log, incident  # important import  # noqa: F401

from fastapi.middleware.cors import CORSMiddleware


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