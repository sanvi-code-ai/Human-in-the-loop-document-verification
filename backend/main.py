from fastapi import FastAPI
from backend.database import Base, engine
from backend import models

app = FastAPI()

Base.metadata.create_all(bind=engine)  #tells SQLAlchemy to create the tables defined in models

@app.get("/")
def home():
    return {"message": "HITL Document Verification API is running"}