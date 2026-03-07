from datetime import datetime
def formatada_nome(nome):
    return nome.title()
def formata_telefone(telefone):
    ddd = telefone[:2]
    numero = telefone[2:]
    numero_formatado = f'({ddd}){numero[:4]}-{numero[5:]}'
    return numero_formatado
def formata_data(data):
    return datetime.strptime(data,'%d/%m/%Y').date()
