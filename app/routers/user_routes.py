from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.auth import create_access_token
from app.models.user import UserCreate, UserOut
from app.crud.user import create_user, get_user_by_email, verify_password

router = APIRouter(prefix="/users", tags=["Usuários"])



@router.post(
    "/",
    response_model=UserOut,
    description="Registro de um novo usúario no banco"
)
async def register(user: UserCreate):
    return await create_user(user)

@router.post(
    "/login",
    description="Login do user e geração de token")
async def login (form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    
    token = create_access_token({"sub": user["email"]})

    return JSONResponse(status_code=200, content={"access_token": token, "token_type": "bearer"})
