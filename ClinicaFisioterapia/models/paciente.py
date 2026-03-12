import utils.validadores as validador
import utils.formatadores as formatador

class Paciente():
    def __init__(self, nome, telefone,data_nascimento,endereco,id=None):
            self._id = id
            self._nome = nome
            self._telefone = telefone
            self._data_nascimento = data_nascimento
            self._endereco = endereco
    # GETTERS 
    def get_id(self):
        return self._id
    def get_nome(self):
        return self._nome
    def get_telefone(self):
        return self._telefone
    def get_data_nascimento(self):
        return self._data_nascimento
    def get_endereco(self):
        return self._endereco
    # SETTERS
    def set_nome(self, novo_nome):
        nome_formatado = formatador.formatada_nome(
            validador.valida_nome(novo_nome)
        )
        self._nome = nome_formatado
    def set_telefone(self, novo_numero):
        telefone_formatado = formatador.formata_telefone(
            validador.valida_telefone(novo_numero)
        )
        self._telefone = telefone_formatado
    def set_data_nascimento(self, nova_data):
        data_formatada = formatador.formata_data(
            validador.valida_data_nascimento(nova_data)
        )
        self._data_nascimento = data_formatada
    def set_endereco(self, novo_endereco):
        endereco_validado = validador.valida_endereco(novo_endereco)
        self._endereco = endereco_validado
