from sqlalchemy.orm import Session
from repository.agendamento_repository import criar_agendamento, buscar_hora
from models.agendamento import Agendamento
from Services.paciente_service import buscar_paciente_por_id
from Services.profissonal_service import buscar_por_id
from utils.validadores import valida_data, valida_hora, valida_status_pagamento, valida_status_agendamento


def buscar_horario(db: Session, hora: str):
    hora_validada = valida_hora(hora)
    return buscar_hora(db, hora_validada)


def criar_agendamento_service(db: Session, dados):
    hora_validada = valida_hora(dados.hora)
    data_validada = valida_data(dados.data)

    agendamento_existente = buscar_horario(db, hora_validada)

    if agendamento_existente:
        raise ValueError("Não é possível marcar nesse horário!")
    

    paciente = buscar_paciente_por_id(db, dados.id_paciente)
    if not paciente:
        raise Exception("Paciente não existente.")
    
    profissional = buscar_por_id(db, dados.id_profissional)
    if not profissional:
        raise Exception("Profissional não existente.")
    

    novo_agendamento = Agendamento(
        id_paciente=dados.id_paciente,
        id_profissional=dados.id_profissional,
        data=data_validada,
        hora=hora_validada,
        status=dados.status,
        status_pagamento=dados.status_pagamento
    )

    return criar_agendamento(db, novo_agendamento)