from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

# Archivos creados previamente
from db.database import get_session
from models.user_model import User
from schemas.user_schema import UserCreate, UserUpdate, UserResponse

# Importar función para encriptar contraseñas
from core.security import get_password_hash

router = APIRouter()

# === CREAR USUARIO ===

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_session)
):
    # Verificar si el email ya existe
    statement = select(User).where(User.email == user.email)
    existing_user = db.exec(statement).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="El correo ya está registrado"
        )

    # Verificar si el username ya existe
    statement = select(User).where(User.username == user.username)
    existing_username = db.exec(statement).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="El nombre de usuario ya está en uso"
        )

    # Hashear la contraseña antes de guardarla
    hashed_password = get_password_hash(user.password)

    # Crear el usuario
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_active=True
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# === ACTUALIZAR USUARIO ===

@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_session)
):
    # Buscar usuario
    db_user = db.get(User, user_id)

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    # Actualizar únicamente los campos proporcionados
    update_data = user_update.model_dump(exclude_unset=True)

    # Si se actualiza la contraseña, hashearla
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(
            update_data.pop("password")
        )

    # Aplicar cambios
    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# === ELIMINAR USUARIO ===

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
    user_id: int,
    session: Session = Depends(get_session)
):
    """
    Elimina un usuario de la base de datos.
    """

    db_user = session.get(User, user_id)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con ID {user_id} no encontrado"
        )

    session.delete(db_user)
    session.commit()

    return None