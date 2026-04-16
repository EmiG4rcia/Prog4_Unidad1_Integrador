from typing import List, Optional
from .schemas import ClienteCreate, ClienteRead

db_clientes: List[ClienteRead] = [
    ClienteRead(id=1, nombre="Juan Pérez", email="juan@example.com", telefono="+54 261 123-4567", activo=True),
    ClienteRead(id=2, nombre="María García", email="maria@example.com", telefono="+54 261 987-6543", activo=True),
]
id_counter = 3


def crear(data: ClienteCreate) -> ClienteRead:
    global id_counter
    nuevo = ClienteRead(id=id_counter, **data.model_dump())
    db_clientes.append(nuevo)
    id_counter += 1
    return nuevo


def obtener_todos(skip: int = 0, limit: int = 10) -> List[ClienteRead]:
    return db_clientes[skip: skip + limit]


def obtener_por_id(id: int) -> Optional[ClienteRead]:
    for c in db_clientes:
        if c.id == id:
            return c
    return None


def actualizar_total(id: int, data: ClienteCreate) -> Optional[ClienteRead]:
    for index, c in enumerate(db_clientes):
        if c.id == id:
            actualizado = ClienteRead(id=id, **data.model_dump())
            db_clientes[index] = actualizado
            return actualizado
    return None


def desactivar(id: int) -> Optional[ClienteRead]:
    for index, c in enumerate(db_clientes):
        if c.id == id:
            c_dict = c.model_dump()
            c_dict["activo"] = False
            actualizado = ClienteRead(**c_dict)
            db_clientes[index] = actualizado
            return actualizado
    return None