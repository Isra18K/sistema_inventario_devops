from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Sistema de Inventario Activo", "estado": "Operativo"}
