from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from routers import Users



# Carga las credenciales desde el archivo JSON que descargaste
cred = credentials.Certificate("ants-97.json")

# Inicializa la aplicación Firebase con las credenciales
firebase_app = firebase_admin.initialize_app(cred, {
        "databaseURL": "https://ants-978b7-default-rtdb.firebaseio.com",
})

app = FastAPI()

#routers
app.include_router(Users.router)
