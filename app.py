from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from pydantic import BaseModel


# Carga las credenciales desde el archivo JSON que descargaste
cred = credentials.Certificate("ants-97.json")

# Inicializa la aplicación Firebase con las credenciales
firebase_app = firebase_admin.initialize_app(cred, {
        "databaseURL": "https://ants-978b7-default-rtdb.firebaseio.com",
})

app = FastAPI()




class Users(BaseModel):
    name: str
    email: str
    password:str
    
# Funciones del controlador
@app.post("/usuario/")
def crear_usuario(user: Users):
    # Convierte el objeto Usuario a un diccionario
    usuario_dict = user.dict()
    
    ref= db.reference('Usuario')
    
    # Envía el usuario a la base de datos de Firebase bajo el nodo "usuarios"
    ref.push(usuario_dict)
    

@app.get("/usuarios/")
async def obtener_usuarios():
    ref= db.reference('Usuario')
    
    return ref.get()


@app.put("/usuario/{id}")
def actualizar_usuario(id: str ,user: Users):    
    ref= db.reference('Usuario')
    user_ref= ref.child(id)
    
    user_ref.update({
        'name': user.name,
        'email': user.email,
        'password': user.password
    })
    
@app.delete("/usuario/{id}")
def eliminar_usuario(id: str):    
    ref= db.reference('Usuario')
    user_ref= ref.child(id)
    
    user_ref.delete()

