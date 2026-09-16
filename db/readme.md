# Módulo de Base de Datos (`db/`)

Gestiona la conexión y la sesión con la base de datos.

- **`database.py`**: Define el `engine` de SQLAlchemy/SQLModel que se conecta al archivo SQLite `mikedb.db`, la función creadora de tablas (`SQLModel.metadata.create_all`) y las dependencias para inyectar la sesión (`Session`) en los endpoints.
