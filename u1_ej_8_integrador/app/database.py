from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
from sqlalchemy import URL

connection_string = URL.create(
    drivername="postgresql",
    username="postgres",
    password="4815162342",
    host="localhost",
    port=5432,
    database="prog4_unidad2"
)

engine = create_engine(connection_string, echo=True)


def create_db_and_tables():
    from app.modules.categoria.models import Categoria
    from app.modules.producto.models import Producto
    from app.modules.cliente.models import Cliente
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session