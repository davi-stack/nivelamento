from fastapi import FastAPI

app = FastAPI()

@app.get("/operadoras/{query}")
def get_operadoras():
    return {
        "operadoras": [
            {"id": 1, "nome": "Operadora A", "cnpj": "12345678000199"},
            {"id": 2, "nome": "Operadora B", "cnpj": "98765432000188"}
        ]
    }
