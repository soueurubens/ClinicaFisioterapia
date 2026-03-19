from database.conexao import Base
from sqlalchemy import Column, String, Integer
class Profissional(Base):
    __tablename__ = 'profissionais'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nomeCompleto = Column(String(90), nullable=False)
    telefone = Column(String(14), nullable=False, unique=True)
    cargo = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False, unique=True)
    crefito = Column(String(30), nullable=False, unique=True)
