from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from routers import Users
from fastapi.middleware.cors import CORSMiddleware




# Carga las credenciales desde el archivo JSON que descargaste
cred = credentials.Certificate("ants-97.json")

# Inicializa la aplicación Firebase con las credenciales
firebase_app = firebase_admin.initialize_app(cred, {
        "databaseURL": "https://ants-978b7-default-rtdb.firebaseio.com",
})

app = FastAPI()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura CORS para permitir solicitudes desde la URL de tu aplicación Expo.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:19006"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#routers
app.include_router(Users.router)
