from fastapi import APIRouter, HTTPException, Path, Query, Depends, status
from sqlmodel import Session
from typing import List
from . import schemas, services
from app.database import get_session

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post(
    "/", response_model=schemas.ClienteRead, status_code=status.HTTP_201_CREATED
)
def alta_cliente(cliente: schemas.ClienteCreate, session: Session = Depends(get_session)):
    return services.crear(session, cliente)


@router.get(
    "/", response_model=List[schemas.ClienteRead], status_code=status.HTTP_200_OK
)
def listar_clientes(skip: int = Query(0, ge=0), limit: int = Query(10, le=50), session: Session = Depends(get_session)):
    return services.obtener_todos(session, skip, limit)


@router.get(
    "/{id}", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK
)
def detalle_cliente(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    cliente = services.obtener_por_id(session, id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return cliente


@router.put(
    "/{id}", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK
)
def actualizar_cliente(cliente: schemas.ClienteCreate, id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    actualizado = services.actualizar_total(session, id, cliente)
    if not actualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return actualizado


@router.put(
    "/{id}/desactivar", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK
)
def borrado_logico(id: int = Path(..., gt=0), session: Session = Depends(get_session)):
    desactivado = services.desactivar(session, id)
    if not desactivado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return desactivado