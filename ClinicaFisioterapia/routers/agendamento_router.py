from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.conexao import get_db
from schemas.agendamento_schema import AgendamentoCreate
from Services.agendamento_service import criar_agendamento_service

router = APIRouter(prefix="/agendamentos", tags=["Agendamentos"])

@router.post("/")
def criar_agendamento(dados: AgendamentoCreate, db: Session = Depends(get_db)):
    try:
        return criar_agendamento_service(db, dados)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))