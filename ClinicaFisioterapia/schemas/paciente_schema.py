from pydantic import BaseModel, EmailStr
from typing import Optional
class PacienteCreate(BaseModel):
    nomeCompleto: str
    cpf: str
    telefone: str
    email: str
    senha: str

class PacienteUpdate(BaseModel):
    nomeCompleto: Optional[str] = None
    cpf: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None