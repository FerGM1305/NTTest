from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from NumerosNaturales import NumeroConjunto100, NumeroRequest 

app = FastAPI()

conjunto = NumeroConjunto100()

# Ruta para extraer un número
@app.post("/extraer/")
async def extraer_numero(request: NumeroRequest):
    try:
        conjunto.extract(request.numero)
        return {"message": f"Número {request.numero} extraído correctamente."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Ruta para obtener el número faltante
@app.get("/faltante/")
async def numero_faltante():
    numero_faltante = conjunto.calcular_numero_faltante()
    return {"numero_faltante": numero_faltante}
