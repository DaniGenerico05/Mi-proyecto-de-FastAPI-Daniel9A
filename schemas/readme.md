# Módulo de Esquemas / DTOs (`schemas/`)

Contiene los modelos de Pydantic/SQLModel utilizados exclusivamente para la entrada y salida de datos (Data Transfer Objects).

- **`user_schema.py`**: Esquemas como `UserCreate` (para recibir contraseñas en texto plano durante el registro) y `UserRead` (para devolver información de usuarios al cliente filtrando la contraseña).
