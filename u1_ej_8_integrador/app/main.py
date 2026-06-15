from fastapi import FastAPI
from app.modules.producto.routers import router as producto_router
from app.modules.categoria.routers import router as categoria_router
from app.modules.cliente.routers import router as cliente_router
from app.database import create_db_and_tables

def create_app() -> FastAPI:
    app = FastAPI(
        title="API Integradora - Unidad 2",
        description="Migración a PostgreSQL con SQLModel.",
        version="2.0.0"
    )

    @app.on_event("startup")
    def on_startup():
        create_db_and_tables()

    app.include_router(producto_router)
    app.include_router(categoria_router)
    app.include_router(cliente_router)

    return app

app = create_app()