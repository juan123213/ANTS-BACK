from modelos.User import User
from fastapi import APIRouter
from firebase_admin import db
from uuid import UUID, uuid4



router = APIRouter()

@router.post("/usuario/")
async def crear_usuario(user: User):
    # Genera un nuevo UUID para el usuario
    user_id = uuid4()

    # Convierte el objeto Usuario a un diccionario
    usuario_dict = user.dict()
    
    # Asigna el ID generado al campo 'id' del diccionario del usuario
    usuario_dict["id"] = str(user_id)
    
    ref= db.reference('Usuario')
    # Envía el usuario a la base de datos de Firebase bajo el nodo "usuarios"
    ref.push(usuario_dict)
    return {"message": "Usuario creado exitosamente"}

@router.get("/usuarios/")
async def obtener_usuarios():
    ref= db.reference('Usuario')
    
    return ref.get()


@router.put("/usuario/{id}")
def actualizar_usuario(id: str ,user: User):    
    ref= db.reference('Usuario')
    user_ref= ref.child(id)
    
    user_ref.update({
        'name': user.name,
        'email': user.email,
        'password': user.password
    })
    
@router.delete("/usuario/{id}")
def eliminar_usuario(id: str):    
    ref= db.reference('Usuario')
    user_ref= ref.child(id)
    
    user_ref.delete()


