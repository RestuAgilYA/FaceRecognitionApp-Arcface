from fastapi import FastAPI
from app.api import endpoints
from app.db.models import Base
from app.db.database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()
app.include_router(endpoints.router)

# Sajikan HTML statis
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse)
def serve_home():
    return os.path.join("frontend", "index.html")

Base.metadata.create_all(bind=engine)
app.include_router(endpoints.router)

@app.get("/")
def root():
    return {"message": "Face Recognition API is running"}