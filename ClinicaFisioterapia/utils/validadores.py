from datetime import datetime
from enums.cargo_enum import CargoEnum
from enums.status_agendamento_enum import status_agendamento
from enums.status_pagamento_enum import status_pagamento


def valida_email(email):
    email = email.strip().lower()

    if "@" not in email or "." not in email:
        raise ValueError("Email inválido.")
    
    return email
def valida_nome(nome: str):
    nome = nome.strip()
    if len(nome) < 10:
        raise ValueError("O nome deve conter no mínimo 10 caracteres.")
    return nome.strip().title()
def valida_telefone(telefone):
    telefone = telefone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if(not telefone or len(telefone.strip()) != 11):
        raise ValueError("O telefone deve ter 11 numeros.")
    if not telefone.isdigit():
        raise ValueError("O telefone não deve haver letras.")
    return telefone
def valida_data_nascimento(data):
    if((data[2] != '/') or (data[5] != '/') or (len(data.strip()) != 10)):
        raise ValueError("Formtado da data DD/MM/AAAA")
    try:
        data_convertida = datetime.strptime(data,'%d/%m/%Y')
    except ValueError:
        raise ValueError("Data inexistente")
    
    if data_convertida > datetime.now():
        raise ValueError("Data de nascimento não pode ser no futuro")
    return data
def valida_endereco(endereco):
    if not endereco or endereco.strip() == "" or len(endereco) < 2:
        raise ValueError("Endereço não pode ser vazio")
    return endereco.strip()
def validar_cargo(cargo):
    try:
        return CargoEnum(cargo.lower())
    except:
        raise ValueError("Cargo inválido.")
def valida_senha(senha):
    senha = senha.strip()
    if len(senha) < 8: 
        raise ValueError("Senha deve conter mais de 8 caracteres.")

    return senha
def valida_cpf(cpf: str):
    cpf_limpo = cpf.replace(".", "").replace("-", "").strip()

    if len(cpf_limpo) != 11:
        raise ValueError("CPF inválido")

    return cpf_limpo

# CREFITO VALIDADORES
def separar_crefito(crefito: str):
    try:
        parte_regiao, resto = crefito.split("-")
        numero, tipo = resto.split("/")

        return parte_regiao, numero, tipo

    except ValueError:
        raise ValueError("Formato inválido de CREFITO. Use: 00-000000/F")
def valida_regiao(regiao):
    if not regiao.isnumeric():
        raise ValueError("Região deve ser numérica (1-20).")

    regiao = int(regiao)

    if regiao < 1 or regiao > 20:
        raise ValueError("Região inválida. Use valores de 1 a 20.")

    return regiao
def valida_numero_crefito(numero):
    numero = numero.strip()

    if not numero.isnumeric():
        raise ValueError("Número do Crefito deve conter apenas números.")

    if len(numero) != 6:
        raise ValueError("Número do Crefito deve ter exatamente 6 dígitos.")

    return numero
def valida_tipo_crefito(tipo):
    tipo = tipo.strip().upper()

    if not tipo.isalpha():
        raise ValueError("Tipo deve conter apenas letras.")

    if len(tipo) != 1:
        raise ValueError("Tipo deve conter apenas uma letra. Ex: 'F'.")

    return tipo
def valida_crefito_completo(crefito: str):
    regiao, numero, tipo = separar_crefito(crefito)

    regiao = valida_regiao(regiao)
    numero = valida_numero_crefito(numero)
    tipo = valida_tipo_crefito(tipo)

    return f"{regiao}-{numero}/{tipo}"

# AGENDAMENTO 
def valida_status_pagamento(status):
    status = status.lower().strip()
    for state in status_pagamento:
        if status == state.value:
            return state
    raise ValueError("ERRO > Status de pagamento inválido.")
def valida_status_agendamento(status):
    status = status.lower().strip()
    for state in status_agendamento:
        if status == state.value:
            return state
    raise ValueError("ERRO > Status de agendamento inválido.")
def valida_data(data):
    if((data[2] != '/') or (data[5] != '/') or (len(data.strip()) != 10)):
        raise ValueError("Data inválida >> Formtado da data DD/MM/AAAA")
    try:
        data_convertida = datetime.strptime(data,'%d/%m/%Y')
        if data_convertida < datetime.now():
            raise ValueError("Data inválida >> Data no passado")
    except ValueError:
        raise ValueError("Data inválida >> Data inexistente")
    return data
def valida_hora(hora_str):
    try:
        datetime.strptime(hora_str, '%H:%M')
        return hora_str
    except ValueError:
        raise ValueError("ERRO >> Hora inválida.")