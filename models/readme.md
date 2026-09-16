# Módulo de Modelos (`models/`)

Define las entidades que se mapean directamente a tablas físicas en la base de datos.

- **`user_model.py`**: Clase `User` definida con `SQLModel(table=True)` que representa la estructura de la tabla de usuarios en `mikedb.db` (campos como `id`, `username`, `email`, `hashed_password`).
