from database.conexao import Base
from sqlalchemy import Column, Enum, Integer, Time, ForeignKey, Date, String
from enums.status_agendamento_enum import status_agendamento as StatusAgendamento
from enums.status_pagamento_enum import status_pagamento as StatusPagamento


class Agendamento(Base):
    __tablename__ = 'agendamentos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # Chaves Estrangeiras
    id_paciente = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    id_profissional = Column(Integer, ForeignKey('profissionais.id'), nullable=False)

    data = Column(String, nullable=False)
    hora = Column(String, nullable=False)

    status = Column(Enum(StatusAgendamento), default=StatusAgendamento.AGENDADA)
    status_pagamento = Column(Enum(StatusPagamento), default=StatusPagamento.PENDENTE)
