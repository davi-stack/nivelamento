from fastapi import FastAPI, Query, HTTPException, status, Request
import pandas as pd
import csv
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite requisições de qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)
def carregar_operadoras():
    operadoras = []
    with open("task3e4/files/operadoras.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")  # Define ";" como delimitador
        for row in reader:
            # Remove aspas extras dos valores
            operadoras.append({k: v.strip().strip('"') for k, v in row.items()})
    return operadoras

dados_operadoras = carregar_operadoras()

# @app.middleware("http")
# async def check_api_key(request: Request, call_next):
#     api_key = request.headers.get("X-API-KEY")
#     if api_key != "your_secret_api_key":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Invalid API Key"
#         )
#     response = await call_next(request)
#     return response

@app.get("/operadoras")
def buscar_operadoras(q: str = Query(..., description="Termo de busca")):
    i = 0
    for op in dados_operadoras:
        print(op)
        if i==5:
            break
    resultado = [
        op for op in dados_operadoras
        if q.lower() in op["Razao_Social"].lower() or q.lower() in op["Nome_Fantasia"].lower()
    ]
    return resultado


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  