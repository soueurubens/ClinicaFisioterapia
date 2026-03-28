from database.conexao import Base
from sqlalchemy import Column, String, Integer, Enum
from enums.cargo_enum import CargoEnum
from sqlalchemy import Enum as SQLEnum
class Profissional(Base):
    __tablename__ = 'profissionais'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nomeCompleto = Column(String(90), nullable=False)
    cargo = Column(SQLEnum(CargoEnum), nullable=False)
    telefone = Column(String(11), nullable=False, unique=True)
    email = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)
    crefito = Column(String(20), nullable=False, unique=True)
