
from pydantic import BaseModel
from uuid import UUID

class Usuario(BaseModel):
    nombre: str
    correo: str
    contraseña:str
    
