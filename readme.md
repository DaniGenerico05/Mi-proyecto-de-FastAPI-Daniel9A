# Práctica de API REST con FastAPI y SQLModel (`lab3`)

Este proyecto consiste en el desarrollo de una API REST utilizando Python y FastAPI, estructurada de manera modular para separar responsabilidades (rutas, seguridad, base de datos, modelos y esquemas).

## 🛠️ Tecnologías y Librerías Utilizadas

- **FastAPI (`fastapi[standard]`)**: Framework principal para la creación de los endpoints HTTP y documentación interactiva.
- **SQLModel**: ORM basado en Pydantic y SQLAlchemy para la interacción con la base de datos.
- **Passlib (`passlib[argon2]`)**: Encriptación y hashing seguro de contraseñas mediante Argon2.
- **SQLite (`mikedb.db`)**: Base de datos relacional liviana basada en archivos.
- **uv**: Gestor de paquetes y entorno virtual ultrarrápido para Python.
- **pip**: Gestor de paquetes complementario para la instalación de dependencias.

## 📁 Estructura del Proyecto

```text
lab3/
├── api/          # Endpoints y rutas de la API (user_api.py)
├── core/         # Configuraciones globales, seguridad y CORS (cors.py, security.py)
├── db/           # Configuración e interacción con SQLite (database.py)
├── models/       # Modelos ORM para tablas de la base de datos (user_model.py)
├── schemas/      # Modelos Pydantic para validación de datos/DTOs (user_schema.py)
├── main.py       # Punto de entrada de la aplicación FastAPI
└── mikedb.db     # Base de datos SQLite local
```

source venv/bin/activate # En Linux/macOS

# o

.\venv\Scripts\activate # En Windows
