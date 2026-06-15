from sqlmodel import Session, select
from typing import List, Optional
from .models import Cliente
from .schemas import ClienteCreate


def crear(session: Session, data: ClienteCreate) -> Cliente:
    cliente = Cliente(**data.model_dump())
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente


def obtener_todos(session: Session, skip: int, limit: int) -> List[Cliente]:
    return session.exec(select(Cliente).offset(skip).limit(limit)).all()


def obtener_por_id(session: Session, id: int) -> Optional[Cliente]:
    return session.get(Cliente, id)


def actualizar_total(session: Session, id: int, data: ClienteCreate) -> Optional[Cliente]:
    cliente = session.get(Cliente, id)
    if not cliente:
        return None
    for key, value in data.model_dump().items():
        setattr(cliente, key, value)
    session.commit()
    session.refresh(cliente)
    return cliente


def desactivar(session: Session, id: int) -> Optional[Cliente]:
    cliente = session.get(Cliente, id)
    if not cliente:
        return None
    cliente.activo = False
    session.commit()
    session.refresh(cliente)
    return cliente