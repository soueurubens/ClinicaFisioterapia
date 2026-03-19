from fastapi import APIRouter, Depends, HTTPException  
from sqlalchemy.orm import Session  

from database.conexao import get_db
from schemas.paciente_schema import PacienteCreate
from Services import paciente_service

router = APIRouter(prefix='/pacientes', tags=["Pacientes"])

@router.get('/')
def listar_pacientes(db: Session = Depends(get_db)):
    return paciente_service.listar_pacientes(db)


@router.delete("/")
def deletar_paciente(paciente_id: int, db: Session = Depends(get_db)):
    try:
        paciente_service.deletar_paciente(db, paciente_id)
        paciente = paciente_service.buscar_paciente_por_id(db, paciente_id)
        return {"mensagem": f"Paciente {paciente.nomeCompleto} deletado."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/")
def criar_paciente(dados: PacienteCreate, db: Session = Depends(get_db)):
    try:
        return paciente_service.criar_paciente(db, dados)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))