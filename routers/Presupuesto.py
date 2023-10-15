from modelos.Presupuesto import Presupuesto
from fastapi import APIRouter
from firebase_admin import db
from uuid import uuid4



router = APIRouter()


@router.post("/presupuesto/")
async def crear_Presupuesto(presupuesto: Presupuesto):
    
    presupuesto_id = uuid4()
    presupuesto.id = str(presupuesto_id)
    presupuesto_dict = presupuesto.dict()    
    
    ref= db.reference('Presupuesto')
    # Envía el Presupuesto a la base de datos de Firebase bajo el nodo "Presupuestos"
    ref.push(presupuesto_dict)
    return {"message": "Presupuesto creado exitosamente"}

@router.get("/presupuestos/")
async def obtener_Presupuestos():    
    ref= db.reference('Presupuesto')
    return ref.get()


