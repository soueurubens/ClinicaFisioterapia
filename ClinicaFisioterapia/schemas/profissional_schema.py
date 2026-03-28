from pydantic import BaseModel
from enums.cargo_enum import CargoEnum
from typing import Optional

class ProfissionalCreate(BaseModel):
    nomeCompleto: str
    telefone: str
    email: str
    cargo: CargoEnum
    senha: str
    crefito: str 

class ProfissionalUpdate(BaseModel):
    nomeCompleto: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    cargo: Optional[CargoEnum] = None
    senha: Optional[str] = None
    crefito: Optional[str] = None 