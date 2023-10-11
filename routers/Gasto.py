from modelos.Gasto import Gasto
from fastapi import APIRouter
from firebase_admin import db
from uuid import uuid4



router = APIRouter()

ref= db.reference('Gasto')


@router.post("/gasto/")
async def crear_gasto(gasto: Gasto):
    # Genera un nuevo UUID para el gasto
    gasto_id = uuid4()

    gasto_dict = gasto.dict()
    
    # Asigna el ID generado al campo 'id' del diccionario del gasto
    gasto_dict["id"] = str(gasto_id)
    
    # Envía el gasto a la base de datos de Firebase bajo el nodo "gastos"
    ref.push(gasto_dict)
    return {"message": "Gasto creado exitosamente"}

@router.get("/gastos/")
async def obtener_gastos():    
    return ref.get()


