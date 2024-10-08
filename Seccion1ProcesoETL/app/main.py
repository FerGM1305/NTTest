from fastapi import FastAPI
from app.routes import data

app = FastAPI()

# Registrar los endpoints
app.include_router(data.router)

@app.get("/")
async def root():
    return {"message": "API para la carga y transformación de datos"}