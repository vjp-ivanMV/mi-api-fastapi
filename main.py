from fastapi import FastAPI
import json

app = FastAPI()

# Cargar datos desde db.json
with open("db.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@app.get("/")
def home():
    return {"mensaje": "API funcionando"}

@app.get("/countries")
def get_data():
    # Accede al valor de la clave 'countries' en el JSON
    # para que devuelva directamente la lista de países.
    return data.get("countries", [])


