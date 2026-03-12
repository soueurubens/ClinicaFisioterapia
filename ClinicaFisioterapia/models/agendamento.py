import utils.formatadores as formatador
import utils.validadores as validador
from enums.status_agendamento_enum import status_agendamento as StatusAgendamento
from enums.status_pagamento_enum import status_pagamento as StatusPagamento

class Agendamento():
    def __init__(self, id_paciente, id_profisional, data, hora, status_pagamento, id_agendamento = None,  status=StatusAgendamento.AGENDADA):
        self._id_agedamento = id_agendamento
        self._id_paciente = id_paciente
        self._id_profissioanl = id_profisional
        self._data = data 
        self._hora = hora
        self._status = status
        self._status_pagamento = status_pagamento
    
    def __str__(self):
        return (
            f'Agendamento[{self._id_agedamento}] | \n'
            f'Paciente: {self._id_paciente} | \n'
            f'Profissional: {self._id_profissioanl} | \n'
            f'Data: {self._data} | \n'
            f'Hora: {self._hora} | \n'
            f'Status: {self._status.value} | \n'
            f'Pagamento: {self._status_pagamento.value} \n'
        )

    # GETTERS 
    def get_id_agendamento(self):
        return self._id_agedamento
    def get_id_paciente(self):
        return self._id_paciente
    def get_id_profissional(self):
        return self._id_profissioanl
    def get_data(self):
        return self._data
    def get_hora(self):
        return self._hora
    def get_status(self):
        return self._status
    def get_status_pagamento(self):
        return self._status_pagamento
    # SETTERS 
    def set_status(self, novo_status):
        status = validador.valida_status_agendamento(novo_status)
        self._status = status
    def set_status_pagamento(self, novo_status):
        status = validador.valida_status_pagamento(novo_status)
        self._status_pagamento = status