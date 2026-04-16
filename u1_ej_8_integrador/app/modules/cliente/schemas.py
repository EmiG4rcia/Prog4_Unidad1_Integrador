from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class ClienteBase(BaseModel):
    nombre: str = Field(..., min_length=2, example="Juan Pérez")
    email: EmailStr = Field(..., example="juan@example.com")
    telefono: str = Field(..., pattern=r"^\+?[\d\s\-]{7,15}$", example="+54 261 123-4567")
    activo: bool = True


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2)
    email: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, pattern=r"^\+?[\d\s\-]{7,15}$")
    activo: Optional[bool] = None


class ClienteRead(ClienteBase):
    id: int