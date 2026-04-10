from database.conexao import Base
from sqlalchemy import Column, Enum, Integer, Time, ForeignKey,String
from enums.status_agendamento_enum import status_agendamento as StatusAgendamento
from enums.status_pagamento_enum import status_pagamento as StatusPagamento

class Atendimento(Base):
    __tablename__ = 'atendimentos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # Chaves Estrangeiras 
    id_agendamento = Column(Integer, ForeignKey('agendamentos.id'), nullable=False)
    
    observacoes = Column(String(500), nullable=True)
    evolucao_clinica = Column(String(500), nullable=False)




