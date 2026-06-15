from sqlmodel import Session, select
from typing import List, Optional
from .models import Categoria
from .schemas import CategoriaCreate


def crear(session: Session, data: CategoriaCreate) -> Categoria:
    categoria = Categoria(**data.model_dump())
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria


def obtener_todas(session: Session, skip: int, limit: int) -> List[Categoria]:
    return session.exec(select(Categoria).offset(skip).limit(limit)).all()


def obtener_por_id(session: Session, id: int) -> Optional[Categoria]:
    return session.get(Categoria, id)


def actualizar_total(session: Session, id: int, data: CategoriaCreate) -> Optional[Categoria]:
    categoria = session.get(Categoria, id)
    if not categoria:
        return None
    for key, value in data.model_dump().items():
        setattr(categoria, key, value)
    session.commit()
    session.refresh(categoria)
    return categoria


def desactivar(session: Session, id: int) -> Optional[Categoria]:
    categoria = session.get(Categoria, id)
    if not categoria:
        return None
    categoria.activo = False
    session.commit()
    session.refresh(categoria)
    return categoria