from fastapi import HTTPException
from app.db.database import db
from app.models.user import UserCreate
from passlib.context import CryptContext
from app.utils.address_validator import validate_address_osm

pwd_context = CryptContext(
    schemes=["bcrypt"], 
    deprecated='auto',
    bcrypt__rounds=12)

async def create_user(user: UserCreate):

    is_valid_address = await validate_address_osm(user.address.model_dump())
    if not is_valid_address:
        raise HTTPException(
            status_code=400,
            detail="Endereço inválido. Verifique os dados informados."
        )

    hashed_pw = pwd_context.hash(user.password)
    user_dict = user.model_dump()
    user_dict['hashed_password'] = hashed_pw
    del user_dict["password"]
    result = await db.user.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict

async def get_user_by_email(email:str):
    user = await db.user.find_one({"email": email})
    if user:
        user["_id"] = str(user["_id"])
    return user

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)