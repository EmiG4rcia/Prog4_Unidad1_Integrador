from sqlmodel import Session
from typing import List, Optional
from .schemas import CategoriaCreate
from .models import Categoria
from . import repository


def crear(session: Session, data: CategoriaCreate) -> Categoria:
    return repository.crear(session, data)


def obtener_todas(session: Session, skip: int = 0, limit: int = 10) -> List[Categoria]:
    return repository.obtener_todas(session, skip, limit)


def obtener_por_id(session: Session, id: int) -> Optional[Categoria]:
    return repository.obtener_por_id(session, id)


def actualizar_total(session: Session, id: int, data: CategoriaCreate) -> Optional[Categoria]:
    return repository.actualizar_total(session, id, data)


def desactivar(session: Session, id: int) -> Optional[Categoria]:
    return repository.desactivar(session, id)