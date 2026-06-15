from sqlmodel import SQLModel, Field
from typing import Optional


class Categoria(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(..., regex=r"^[A-Z]{3}-\d{2}$")
    descripcion: str
    activo: bool = True