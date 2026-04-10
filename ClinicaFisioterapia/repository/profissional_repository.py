from models.profissional import Profissional
from utils.validadores import valida_nome
def criar(db, profissional):
    db.add(profissional)
    db.commit()
    db.refresh(profissional)

    return profissional

def buscar_por_id(db, profissional_id):
    return db.query(Profissional).filter_by(id=profissional_id).first()

def buscar_por_email(db, email_profissional):
    return db.query(Profissional).filter_by(email=email_profissional).first()

def buscar_por_crefito(db, crefito_profissional):
    return db.query(Profissional).filter_by(crefito=crefito_profissional).first()

def deletar(db, profissional: Profissional):
    db.delete(profissional)
    db.commit()

def listar(db):
    return db.query(Profissional).all()




