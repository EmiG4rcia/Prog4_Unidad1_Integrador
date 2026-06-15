from sqlmodel import Session
from typing import List, Optional
from .schemas import ProductoCreate
from .models import Producto
from . import repository


def crear(session: Session, data: ProductoCreate) -> Producto:
    return repository.crear(session, data)


def obtener_todos(session: Session, skip: int = 0, limit: int = 10) -> List[Producto]:
    return repository.obtener_todos(session, skip, limit)


def obtener_por_id(session: Session, id: int) -> Optional[Producto]:
    return repository.obtener_por_id(session, id)


def actualizar_total(session: Session, id: int, data: ProductoCreate) -> Optional[Producto]:
    return repository.actualizar_total(session, id, data)


def desactivar(session: Session, id: int) -> Optional[Producto]:
    return repository.desactivar(session, id)


def obtener_estado_stock(session: Session, id: int) -> Optional[dict]:
    producto = repository.obtener_por_id(session, id)
    if not producto:
        return None
    return {
        "stock": producto.stock,
        "bajo_stock_minimo": producto.stock < producto.stock_minimo,
        "activo": producto.activo,
    }