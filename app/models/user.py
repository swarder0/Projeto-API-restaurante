from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

    @field_validator('*')
    def no_empty_fields(cls, v):
        if not v or not v.strip():
            raise ValueError("Campo obrigatório e não pode estar vazio")
        return v

class UserBase(BaseModel):
    email: EmailStr
    name: str

    @field_validator("name")
    def validate_name(cls, v):
        if len(v) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres")
        if len(v.split()) < 2:
            raise ValueError("Informe nome e sobrenome")
        return v

class UserCreate(UserBase):
    password: str
    phone: str
    address: Address

    @field_validator("phone")
    def validate_phone(cls, v):
        if v is None:
            return v
        digits_only = ''.join(filter(str.isdigit, v))
        if len(digits_only) != 11:
            raise ValueError("O telefone deve ter pelo menos 11 dígitos")
        return v

class UserDB(UserBase):
    hashed_password: str
    phone: Optional[str] = None
    address: Optional[Address]= None

class UserOut(UserBase):
    id: str = Field(..., alias="_id")
    phone: Optional[str] = None
    address: Optional[Address]= None
