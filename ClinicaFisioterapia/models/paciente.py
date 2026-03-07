class Paciente():
    def __init__(self, nome, telefone,data_nascimento,endereco,
                 observacoes,id=None):
            self._id = id
            self._nome = nome
            self._telefone = telefone
            self._data_nascimento = data_nascimento
            self._endereco = endereco
            self._observacoes = observacoes
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
    def get_oberservacoes(self):
        return self._observacoes
    # SETTERS
    def set_nome(self, novo_nome):
        self._nome = novo_nome
    def set_telefone(self, novo_numero):
        self._telefone = novo_numero
    def set_data_nascimento(self, nova_data):
        self._data_nascimento = nova_data
    def set_endereco(self, novo_endereco):
        self._endereco = novo_endereco
    def set_observacoes(self, nova_observacao):
        self._observacoes = nova_observacao