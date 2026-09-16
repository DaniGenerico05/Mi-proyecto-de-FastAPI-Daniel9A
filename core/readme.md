# Módulo Core (`core/`)

Contiene las configuraciones globales, reglas de seguridad y middleware de la aplicación.

- **`cors.py`**: Configuración de políticas CORS (Cross-Origin Resource Sharing) para permitir o restringir peticiones desde diferentes orígenes/dominios.
- **`security.py`**: Lógica de hashing y verificación de contraseñas utilizando `passlib` con el algoritmo Argon2, así como la gestión de tokens o autenticación.
