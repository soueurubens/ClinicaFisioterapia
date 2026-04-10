from datetime import datetime

def email(email):
    return email.lower().strip()
def nome(nome):
    return nome.title()
def telefone(telefone):
    ddd = telefone[:2]
    numero = telefone[2:]
    numero_formatado = f'({ddd}){numero[:4]}-{numero[5:]}'
    return numero_formatado
def data(data):
    return datetime.strptime(data,'%d/%m/%Y').date()
def crefito(regiao, numero, tipo='F'):
    return f'CREFITO-{regiao}/{numero}-{tipo}'

