import utils.validadores as validador
import utils.formatadores as formatador
class Profissional():
    def __init__(self, nome, telefone, cargo, crefito, email, id=None):
        self._id = id
        self._nome = nome
        self._telefone = telefone
        self._cargo = cargo
        self._crefito = crefito
        self._email = email

    def __str__(self):
        return (
            f'ID: {self._id} | '
            f'Nome: {self._nome} | '
            f'Cargo: {self._cargo.value} | '
            f'CREFITO: {self._crefito} | '
            f'Telefone: {self._telefone} | '
            f'Email: {self._email}'
        )

    def get_nome(self):
        return self._nome
    def get_telefone(self):
        return self._telefone
    def get_cargo(self):
        return self._cargo
    def get_id(self):
        return self._id
    def get_crefito(self):
        return self._crefito
    def get_email(self):
        return self._email

    def set_nome(self, novo_nome):
        nome_formatado = formatador.formata_nome(validador.valida_nome(novo_nome))
        self._nome = nome_formatado
    def set_telefone(self, novo_telefone):
        telefone_formatado = formatador.formata_telefone(validador.valida_telefone(novo_telefone))
        self._telefone = telefone_formatado
    def set_cargo(self, novo_cargo):
        cargo_formatado = validador.valida_cargo(novo_cargo)
        self._cargo = cargo_formatado
    def set_email(self, novo_email):
        email = formatador.formata_email(validador.valida_email(novo_email))
        self._email = email
