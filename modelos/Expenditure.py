from pydantic import BaseModel
from datetime import date

class Expenditure(BaseModel):
    description: str
    amount: float
    date: date
    
    
    
