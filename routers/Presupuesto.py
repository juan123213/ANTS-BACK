from modelos.Presupuesto import Presupuesto
from fastapi import APIRouter
from firebase_admin import db
from uuid import uuid4
from datetime import date
from datetime import datetime

router = APIRouter()

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

@router.get("/presupuestos/{fecha}")
async def obtenerPresupuestos(fecha: str):    
    ref = db.reference('Presupuesto')
    presupuestos = ref.get()
    
    if presupuestos:
        presupuestos_mes = [p for p in presupuestos.values() if p["fecha"] == fecha]
        
        if presupuestos_mes:
            return presupuestos_mes
        else:
            return {"message": f"No se encontraron presupuestos para el mes {fecha}"}
    else:
        return {"message": "No hay presupuestos registrados"}