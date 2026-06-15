from sqlmodel import Session
from typing import List, Optional
from .schemas import ClienteCreate
from .models import Cliente
from . import repository


def crear(session: Session, data: ClienteCreate) -> Cliente:
    return repository.crear(session, data)


def obtener_todos(session: Session, skip: int = 0, limit: int = 10) -> List[Cliente]:
    return repository.obtener_todos(session, skip, limit)


def obtener_por_id(session: Session, id: int) -> Optional[Cliente]:
    return repository.obtener_por_id(session, id)


def actualizar_total(session: Session, id: int, data: ClienteCreate) -> Optional[Cliente]:
    return repository.actualizar_total(session, id, data)


def desactivar(session: Session, id: int) -> Optional[Cliente]:
    return repository.desactivar(session, id)