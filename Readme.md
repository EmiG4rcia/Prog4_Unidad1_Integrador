
## Configuración de la base de datos

1. Asegurate de que PostgreSQL esté corriendo en tu máquina.

2. Creá la base de datos (si aún no existe):

```sql
CREATE DATABASE prog4_unidad2;
```

3. Revisá los datos de conexión en `u1_ej_8_integrador/app/database.py` y ajustalos según tu entorno local:

| Parámetro  | Valor por defecto |
|------------|-------------------|
| Host       | `localhost`       |
| Puerto     | `5432`            |
| Usuario    | `postgres`        |
| Contraseña | *(configurar)*    |
| Base       | `prog4_unidad2`   |

> Al iniciar la aplicación, las tablas se crean automáticamente mediante `create_db_and_tables()`.

## Instalación

Desde la carpeta raíz del repositorio (`fastapi_backend`):

### 1. Crear y activar el entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

> **Importante:** el servidor debe levantarse desde la carpeta `u1_ej_8_integrador`, no desde la raíz del repo.

```powershell
cd u1_ej_8_integrador
```

### Opción A — Modo desarrollo (recomendado)

```bash
fastapi dev app/main.py
```

Si todo salió bien, verás un mensaje similar a:

```
Server started at http://127.0.0.1:8000
Documentation at http://127.0.0.1:8000/docs

```