from datetime import datetime

def valida_nome(nome):
    if(not nome or len(nome.strip()) < 3):
        raise ValueError("Nome inválido >> Deve ter no minimo 3 caracteres.")
    if not nome.replace(" ", "").isalpha():
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
