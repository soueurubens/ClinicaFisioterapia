from fastapi import APIRouter, Depends, HTTPException  
from sqlalchemy.orm import Session  

from database.conexao import get_db
from schemas.paciente_schema import PacienteCreate, PacienteUpdate
from Services import paciente_service

router = APIRouter(prefix='/pacientes', tags=["Pacientes"])

@router.put('/{paciente_id}')
def atualizar_paciente(paciente_id: int, dados: PacienteUpdate, db: Session = Depends(get_db)):
    try: 
        paciente = paciente_service.atualizar_paciente(db, dados, paciente_id)
        return paciente
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
@router.get('/')
def listar_pacientes(db: Session = Depends(get_db)):
    return paciente_service.listar_pacientes(db)
@router.delete('/{paciente_id}')
def deletar_paciente(paciente_id: int, db: Session = Depends(get_db)):
    try:
        return paciente_service.deletar_paciente(db, paciente_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.post("/")
def criar_paciente(dados: PacienteCreate, db: Session = Depends(get_db)):
    try:
        paciente = paciente_service.criar_paciente(db, dados)
        return {
            "mensagem": "Paciente criado com sucesso.",
            "paciente": {
                "id": paciente.id,
                "nomeCompleto": paciente.nomeCompleto,
                "cpf": paciente.cpf,
                "email": paciente.email,
                "telefone": paciente.telefone
            }
        }

    except ValueError as e:
            print("VALUEERROR:", repr(e))
            raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        print("EXCEPTION:", type(e), repr(e))
        raise HTTPException(status_code=500, detail=str(e))