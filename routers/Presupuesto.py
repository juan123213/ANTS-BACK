from modelos.Presupuesto import Presupuesto
from fastapi import APIRouter
from firebase_admin import db
from uuid import uuid4
from datetime import date
from datetime import datetime

router = APIRouter()

def fecha_a_string(fecha: date) -> str:
    """Convierte una fecha en un formato de string."""
    return fecha.strftime("%Y-%m-%d") if fecha else None

@router.post("/presupuesto/")
async def crear_Presupuesto(presupuesto: Presupuesto):
    
    presupuesto_id = uuid4()
    presupuesto.id = str(presupuesto_id)



    presupuesto_dict = presupuesto.dict()    
    
    ref = db.reference('Presupuesto')
    # Envía el Presupuesto a la base de datos de Firebase bajo el nodo "Presupuestos"
    ref.push(presupuesto_dict)
    return {"message": "Presupuesto creado exitosamente"}

@router.get("/presupuestos/")
async def obtenerPresupuestos():    
    ref = db.reference('Presupuesto')
    return ref.get()

@router.get("/presupuestos/{mes_anio}")
async def obtenerPresupuestos(mes_anio: str):    
    ref = db.reference('Presupuesto')
    return ref.get()
