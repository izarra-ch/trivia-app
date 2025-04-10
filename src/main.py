import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
  return {"server": "Servidor iniciado"}
