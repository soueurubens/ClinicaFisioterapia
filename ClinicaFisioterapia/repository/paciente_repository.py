from models.paciente import Paciente
from sqlalchemy.exc import IntegrityError

def criar(db, paciente: Paciente):
    try: 
        db.add(paciente)
        db.commit()
        db.refresh(paciente)
        return paciente

    except IntegrityError:
        db.rollback()
        raise ValueError("Paciente já cadastrado.")
def busca_por_id(db, idPaciente: int):
    paciente = db.get(Paciente, idPaciente)
    return paciente
def buscar_por_nome(db, nomePaciente: str):
    paciente = db.query(Paciente).filter(
        Paciente.nomeCompleto.ilike(f'%{nomePaciente}%')
        ).first()
    return paciente
def deletar(db, paciente: Paciente):
    db.delete(paciente)
    db.commit()
def listar(db):
    return db.query(Paciente).all()