from models.paciente import Paciente
from repository import paciente_repository
import utils.validadores as Validador

def atualizar_paciente(db, dados, paciente_id):
    paciente = buscar_paciente_por_id(db,paciente_id)
    
    if dados.nomeCompleto is not None:
        paciente.nomeCompleto = Validador.valida_nome(dados.nomeCompleto.strip().title())

    if dados.cpf is not None:
        paciente.cpf = Validador.valida_cpf(dados.cpf.replace('.', "").replace("-", "").strip())
    
    if dados.telefone is not None:
        paciente.telefone = Validador.valida_telefone((
            dados.telefone
            .replace("(", "")
            .replace(")", "")
            .replace("-","")
            .strip()
        ))
    if dados.email is not None:
        paciente.email = Validador.valida_email(dados.email.strip().lower())
    
    if dados.senha is not None:
        paciente.senha = Validador.valida_senha(dados.senha)
    
    db.commit()
    db.refresh(paciente)

    return paciente
def criar_paciente(db, dados):
    _nome = Validador.valida_nome(dados.nomeCompleto)
    _cpf = Validador.valida_cpf(dados.cpf)
    _telefone = Validador.valida_telefone(dados.telefone)
    _email = Validador.valida_email(dados.email)
    _senha = Validador.valida_senha(dados.senha)

    if paciente_repository.buscar_por_cpf(db, _cpf):
        raise ValueError("CPF já cadastrado!")

    if paciente_repository.buscar_por_email(db, _email):
        raise ValueError("Email já cadastrado!")

    novo_paciente = Paciente(
        nomeCompleto=_nome,
        cpf=_cpf,
        telefone=_telefone,
        email=_email,
        senha=_senha
    )

    return paciente_repository.criar(db, novo_paciente)
def buscar_paciente_por_id(db, paciente_id: int):
    paciente = paciente_repository.busca_por_id(db, paciente_id)
    if paciente is None:
        raise ValueError("Paciente não encontrado.")
    return paciente
def deletar_paciente(db, paciente_id):
    paciente = buscar_paciente_por_id(db, paciente_id)

    try:
        paciente_repository.deletar(db, paciente)
        return {"mensagem": f"{paciente.nomeCompleto} deletado com sucesso."}
    except Exception as e:
        db.rollback()
        raise Exception(f"Erro ao deletar paciente: {str(e)}")
def listar_pacientes(db):
    lista = paciente_repository.listar(db)
    if len(lista) < 1:
        raise ValueError("Lista vazia!")
    return lista
