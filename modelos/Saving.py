from pydantic import BaseModel
from datetime import date

class Saving(BaseModel):
    description: str
    amount: float
    date: date
    
    
    
