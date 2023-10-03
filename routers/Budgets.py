from modelos.Budget import Budget
from fastapi import APIRouter
from firebase_admin import db


router = APIRouter()

@router.post("/budget/")
def crear_usuario(budget: Budget):
    
    budget.id = str(budget.id)
    # Convierte el objeto Usuario a un diccionario
    usuario_dict = budget.dict()
    
    ref= db.reference('Usuario')
    # Envía el usuario a la base de datos de Firebase bajo el nodo "usuarios"
    ref.push(usuario_dict)
    

@router.get("/usuarios/")
async def obtener_usuarios():
    ref= db.reference('Usuario')
    
    return ref.get()


@router.put("/usuario/{id}")
def actualizar_usuario(id: str ,Budget: Budget):    
    ref= db.reference('Usuario')
    Budget_ref= ref.child(id)
    
    Budget_ref.update({
        'name': Budget.name,
        'email': Budget.email,
        'password': Budget.password
    })
    
@router.delete("/usuario/{id}")
def eliminar_usuario(id: str):    
    ref= db.reference('Usuario')
    Budget_ref= ref.child(id)
    
    Budget_ref.delete()


