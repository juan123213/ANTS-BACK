from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Carga las credenciales desde el archivo JSON que descargaste
cred = credentials.Certificate("ants-97.json")

# Inicializa la aplicación Firebase con las credenciales
firebase_app = firebase_admin.initialize_app(cred, {
        "databaseURL": "https://ants-978b7-default-rtdb.firebaseio.com",
})

ref = db.reference("/Usuario")

ref.set({
    
    'Usuario1':
        {
            'Nombre': 'Antonio',
            'Edad': 23,
            'Correo': 'juan.giraldo@gmail.com',
            'Telefono': '987654321',
            'Direccion': 'Calle 123',
        }
    
})

data = ref.get()

print(data)



app = FastAPI()

# Define una ruta que devuelva los datos almacenados en la variable "data"
@app.get("/datos-usuario/")
async def obtener_datos_usuario():
    return data