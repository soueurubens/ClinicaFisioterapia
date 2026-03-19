from models.paciente import Paciente
from repository import paciente_repository

def criar_paciente(db, dados):
    paciente = Paciente(
        nomeCompleto=dados.nomeCompleto.lower(),
        cpf=dados.cpf,
        telefone=dados.telefone,
        email=dados.email,
        senha=dados.senha
    )
    return paciente_repository.criar(db, paciente)
def buscar_paciente_por_id(db, paciente_id: int):
    paciente = paciente_repository.busca_por_id(db, paciente_id)
    if(not paciente):
        raise ValueError("Paciente não encontrado.")
    return paciente
def deletar_paciente(db, paciente_id):
    paciente = paciente_repository.busca_por_id(db,paciente_id)
    if not paciente:
        raise ValueError("Paciente não encontrando.")
    paciente_repository.deletar(db, paciente)
def listar_pacientes(db):
    return paciente_repository.listar(db)