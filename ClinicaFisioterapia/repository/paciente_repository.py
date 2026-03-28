from models.paciente import Paciente

def criar(db, paciente: Paciente):
    db.add(paciente)
    db.commit()
    db.refresh(paciente)
    return paciente
def busca_por_id(db, idPaciente: int):
    return db.get(Paciente, idPaciente)
def buscar_por_cpf(db, cpf_cliente):
    return db.query(Paciente).filter_by(cpf=cpf_cliente).first()
def buscar_por_email(db, email_paciente: str):
    return db.query(Paciente).filter_by(email=email_paciente).first()
def deletar(db, paciente: Paciente):
    db.delete(paciente)
    db.commit()
def listar(db):
    return db.query(Paciente).all()