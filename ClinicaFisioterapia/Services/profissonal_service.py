from repository import profissional_repository
from models.profissional import Profissional
from utils.validadores import (
    valida_nome,
    valida_crefito_completo,
    valida_telefone,
    valida_senha,
    valida_email,
    validar_cargo
)
def buscar_por_id(db, id):
    profissional = profissional_repository.buscar_por_id(db, id)
    if not profissional:
        raise ValueError("Profissional não encontrado!")
    return profissional
def buscar_crefito(db, crefito):
    profissional = profissional_repository.buscar_por_crefito(db, crefito)
    if not profissional:
        raise ValueError("Profissional não encotrado!")
    return profissional
def buscar_email(db, email):
    profissional = profissional_repository.buscar_por_email(db, email)
    if not profissional:
        raise ValueError("Profissional não encotrado!")
    return profissional
def cria_profissional(db, dados):
    _nome = valida_nome(dados.nomeCompleto)
    _telefone = valida_telefone(dados.telefone)
    _email = valida_email(dados.email)
    _cargo = dados.cargo
    _senha = valida_senha(dados.senha)
    _crefito = valida_crefito_completo(dados.crefito)

    if profissional_repository.buscar_por_crefito(db, _crefito):
        raise ValueError("Crefito já cadastrado!")
    
    if profissional_repository.buscar_por_email(db, _email):
        raise ValueError("Email já cadastrado!")

    novo_profissional = Profissional(
        nomeCompleto=_nome,
        telefone=_telefone,
        cargo=_cargo,
        email=_email,
        senha=_senha,
        crefito=_crefito
    )

    return profissional_repository.criar(db, novo_profissional)
def listar_profissionais(db):
    lista = profissional_repository.listar(db)
    if len(lista) < 1:
        raise ValueError("Lista vazia!")
    return lista
def deletar_profissional(db, profissional_id):
    profissional = buscar_por_id(db, profissional_id)
    try: 
        profissional_repository.deletar(db, profissional)
        return {"mensagem": f"{profissional.nomeCompleto} deletado com sucesso."}
    except Exception as e:
        db.rollback()
        raise Exception(f"Erro ao deletar profissional: {str(e)}")
def atualizar_profissional(db, dados, profissional_id):
    profissional = profissional_repository.buscar_por_id(db,profissional_id)
    
    if dados.nomeCompleto is not None:
        profissional.nomeCompleto = valida_nome(dados.nomeCompleto.strip().title())

    if dados.cargo is not None:
        profissional.cargo = validar_cargo(dados.cargo)

    if dados.crefito is not None:
        profissional.cpf = valida_crefito_completo(dados.crefito)
    
    if dados.telefone is not None:
        profissional.telefone = valida_telefone((
            dados.telefone
            .replace("(", "")
            .replace(")", "")
            .replace("-","")
            .strip()
        ))
    if dados.email is not None:
        profissional.email = valida_email(dados.email.strip().lower())
    
    if dados.senha is not None:
        profissional.senha = valida_senha(dados.senha)
    
    db.commit()
    db.refresh(Profissional)

    return profissional
