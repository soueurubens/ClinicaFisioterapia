from datetime import datetime
from enums.cargo_enum import Cargo
from enums.status_agendamento_enum import status_agendamento
from enums.status_pagamento_enum import status_pagamento



def valida_email(email):
    if ('@' not in email):
        raise ValueError("ERRO > Email precisa conter @.")
    if len(email.strip()) < 5:
        raise ValueError("ERRO > Email inválido.")
    return email
def valida_nome(nome):
    if(not nome or len(nome.strip()) < 3):
        raise ValueError("Nome inválido >> Deve ter no minimo 3 caracteres.")
    if nome.replace(" ", "").isnumeric():
        raise ValueError("Nome inválido >> Nome não deve conter números.")
    return nome.strip()
def valida_telefone(telefone):
    telefone = telefone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if(not telefone or len(telefone.strip()) < 11):
        raise ValueError("Número inválido >> Deve ter no minimo 11 numeros.")
    if telefone.isalpha():
        raise ValueError("Número inválido >> Não deve haver letras no telefone.")
    return telefone
def valida_data_nascimento(data):
    if((data[2] != '/') or (data[5] != '/') or (len(data.strip()) != 10)):
        raise ValueError("Data inválida >> Formtado da data DD/MM/AAAA")
    try:
        data_convertida = datetime.strptime(data,'%d/%m/%Y')
    except ValueError:
        raise ValueError("Data inválida >> Data inexistente")
    
    if data_convertida > datetime.now():
        raise ValueError("Data de nascimento não pode ser no futuro")
    return data
def valida_endereco(endereco):
    if not endereco or endereco.strip() == "":
        raise ValueError("Endereço não pode ser vazio")
    return endereco.strip()
def valida_cargo(cargo_str):

    for cargo in Cargo:
        if cargo.value == cargo_str.capitalize().strip():
            return cargo
    raise ValueError("Cargo inválido")
def valida_senha(senha):
    if len(senha.strip()) < 5:
        raise ValueError("Senha muito pequena.")
    if len(senha.strip()) > 50:
        raise ValueError("Senha muito grande.")
    if " " in senha.strip():
        raise ValueError("Senha não devo conter espaço.")
    
    

# CREFITO VALIDADORES 
def valida_regiao(regiao):
    if(int(regiao) > 20 or int(regiao) < 1):
        raise ValueError("ERRO > Regiões inválidas. Somente de 1-20")
    if(not regiao.isnumeric()):
        raise ValueError("ERRO >> Região tem que ser numérica de 1-20.")
    return regiao
def valida_numero_crefito(numero):
    if len(numero) < 6: 
        raise ValueError("ERRO >> O número do Crefito precisa ter 6 números.")
    if numero.isalpha():
        raise ValueError("ERRO >> Número do Crefito não pode conter letras.")
    return numero
def valida_tipo_crefito(tipo):
    if len(tipo) > 1 or len(tipo) < 0:
        raise ValueError("ERRO >> A ocupação deve conter uma letra. Ex: 'F'.")
    if tipo.isnumeric():
        raise ValueError("ERRO >> A ocupação deve conter uma letra. Ex: 'F'.")
    return tipo


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