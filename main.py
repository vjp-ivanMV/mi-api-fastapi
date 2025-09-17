from fastapi import FastAPI
import json

app = FastAPI()

# Cargar datos desde db.json
with open("db.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@app.get("/")
def home():
    return {"mensaje": "API funcionando"}

@app.get("/api")
def get_data():
    return data
