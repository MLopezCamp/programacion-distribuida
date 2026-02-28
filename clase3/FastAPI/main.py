# ================================
# IMPORTACIONES
# ================================

from fastapi import FastAPI, HTTPException
from typing import List
import asyncio

# ================================
# CREACIÓN DE LA APLICACIÓN
# ================================

app = FastAPI()

# ================================
# BASE DE DATOS SIMULADA
# ================================

clientes = []  # Lista en memoria
contador_clientes_creados = 0  # Contador global de clientes creados


# ================================
# ENDPOINTS
# ================================

@app.get("/")
def home():
    return {"mensaje": "API del Banco funcionando"}


# ================================
# CREAR CLIENTE (POST)
# ================================

@app.post("/clientes")
async def crear_cliente(nombre: str):

    global contador_clientes_creados

    #Validación básica
    if not nombre.strip():
        raise HTTPException(status_code=400, detail="El nombre no puede estar vacío")

    #Simulación de delay asíncrono
    await asyncio.sleep(3)

    cliente = {
        "id": len(clientes) + 1,
        "nombre": nombre
    }

    clientes.append(cliente)
    contador_clientes_creados += 1

    return {
        "cliente": cliente,
        "total_clientes_creados": contador_clientes_creados
    }


# ================================
# LISTAR CLIENTES (GET)
# ================================

@app.get("/clientes", response_model=List[dict])
def listar_clientes():
    return clientes


# ================================
# OBTENER CLIENTE POR ID (GET)
# ================================

@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente

    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# ================================
# ACTUALIZAR CLIENTE (PUT)
# ================================

@app.put("/clientes/{cliente_id}")
def actualizar_cliente(cliente_id: int, nombre: str):

    if not nombre.strip():
        raise HTTPException(status_code=400, detail="El nombre no puede estar vacío")

    for cliente in clientes:
        if cliente["id"] == cliente_id:
            cliente["nombre"] = nombre
            return {"mensaje": "Cliente actualizado", "cliente": cliente}

    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# ================================
# ELIMINAR CLIENTE (DELETE)
# ================================

@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int):

    for cliente in clientes:
        if cliente["id"] == cliente_id:
            clientes.remove(cliente)
            return {"mensaje": "Cliente eliminado correctamente"}

    raise HTTPException(status_code=404, detail="Cliente no encontrado")