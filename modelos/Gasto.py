from pydantic import BaseModel
from datetime import date


class Gasto(BaseModel):
    cantidad: float
    descricion: str
    fecha:date
    id_usuario: str
    
