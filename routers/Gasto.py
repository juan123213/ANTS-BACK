from modelos.Gasto import Gasto
from fastapi import APIRouter
from firebase_admin import db
from uuid import uuid4
from datetime import datetime

router = APIRouter()
    
@router.post("/gasto/")
async def crear_gasto(gasto: Gasto):
    gasto_id = uuid4()
    gasto.id = str(gasto_id)

    # Establecer el mes y año actual solo si no se proporciona
    if not gasto.fecha:
        gasto.fecha = datetime.now().strftime("%Y-%m")

    gasto_dict = gasto.dict()    
    
    ref = db.reference('Gasto')
    # Envía el gasto a la base de datos de Firebase bajo el nodo "gastos"
    ref.push(gasto_dict)
    return {"message": "Gasto creado exitosamente"}

@router.get("/gastos/")
async def obtener_gastos():    
    ref = db.reference('Gasto')
    return ref.get()