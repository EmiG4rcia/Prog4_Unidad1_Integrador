from sqlmodel import Session, select
from typing import List, Optional
from .models import Producto
from .schemas import ProductoCreate


def crear(session: Session, data: ProductoCreate) -> Producto:
    producto = Producto(**data.model_dump())
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


def obtener_todos(session: Session, skip: int, limit: int) -> List[Producto]:
    return session.exec(select(Producto).offset(skip).limit(limit)).all()


def obtener_por_id(session: Session, id: int) -> Optional[Producto]:
    return session.get(Producto, id)


def actualizar_total(session: Session, id: int, data: ProductoCreate) -> Optional[Producto]:
    producto = session.get(Producto, id)
    if not producto:
        return None
    for key, value in data.model_dump().items():
        setattr(producto, key, value)
    session.commit()
    session.refresh(producto)
    return producto


def desactivar(session: Session, id: int) -> Optional[Producto]:
    producto = session.get(Producto, id)
    if not producto:
        return None
    producto.activo = False
    session.commit()
    session.refresh(producto)
    return producto