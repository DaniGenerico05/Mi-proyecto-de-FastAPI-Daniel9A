# main.py
from contextlib import asynccontextmanager 
from fastapi import FastAPI

#Importacion de archivos previos
from db.database import create_db_and_tables
from api.user_api import *
from core.cors import setup_cors

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    print("Iniciando base de datos...")
    create_db_and_tables()
    yield
   
    print("Cerrando aplicación...")

# Crear la app con lifespan
app = FastAPI(
    title="FastAPI Daniel",
    description="Mi primera API con FastAPI y SQLModel",
    version="1.0.0",
    lifespan=lifespan  
)

# Configurar CORS desde core
setup_cors(app)

# Incluir routers
app.include_router(router, prefix="/api/v1/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "¡Bienvenido a FastAPI de Daniel!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}