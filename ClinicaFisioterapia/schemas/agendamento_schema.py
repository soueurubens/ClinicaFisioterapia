from pydantic import BaseModel
from enums.status_agendamento_enum import status_agendamento as StatusAgendamento
from enums.status_pagamento_enum import status_pagamento as StatusPagamento

class AgendamentoCreate(BaseModel):
    id_paciente: int
    id_profissional: int
    data: str = "Dia/Mês"
    hora: str = "Horas:Minutos"
    status: StatusAgendamento = StatusAgendamento.AGENDADA
    status_pagamento: StatusPagamento = StatusPagamento.PENDENTE