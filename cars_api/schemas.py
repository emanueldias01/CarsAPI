from pydantic import BaseModel
from typing import Optional

class CarRequest(BaseModel):
    brand: str
    model: str
    color: Optional[str] = None
    factory_year: int
    model_year: Optional[int] = None
    description: Optional[str] = None

class CarResponse(BaseModel):
    id: int
    brand: str
    model: str
    color: str
    factory_year: int
    model_year: int
    description: str

class CarList(BaseModel):
    cars: list[CarResponse]

class UserBase(BaseModel):
    login: str
    password: str

class Token(BaseModel):
    token: str