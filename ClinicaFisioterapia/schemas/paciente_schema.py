from pydantic import BaseModel, EmailStr

class PacienteCreate(BaseModel):
    nomeCompleto: str
    cpf: str
    telefone: str
    email: EmailStr
    senha: str