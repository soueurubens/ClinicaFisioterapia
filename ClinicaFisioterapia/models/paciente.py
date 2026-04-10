from database.conexao import Base
from sqlalchemy import Column, String, Integer

class Paciente(Base):
    __tablename__ = 'pacientes'
    # Criando os atributos do paciente 
    id = Column(Integer, primary_key=True, autoincrement=True)
    nomeCompleto = Column(String(90), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    telefone = Column(String(14), nullable=False, unique=True)
    email = Column(String(50), nullable=False)
    senha = Column(String(30), nullable=False)
    