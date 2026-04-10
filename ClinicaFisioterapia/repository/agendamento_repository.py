from sqlalchemy.orm import Session
from models.agendamento import Agendamento


def buscar_hora(db: Session, horas: str):
    return db.query(Agendamento).filter_by(hora=horas).first()

def criar_agendamento(db: Session, dados: Agendamento):
    db.add(dados)
    db.commit()
    db.refresh(dados)
    return dados