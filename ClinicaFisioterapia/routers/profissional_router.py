from fastapi import APIRouter, Depends, HTTPException  
from sqlalchemy.orm import Session  

from database.conexao import get_db
from schemas.profissional_schema import ProfissionalCreate, ProfissionalUpdate
from Services import profissonal_service

router = APIRouter(prefix='/profissionais', tags=["Profissionais"])

@router.post('/')
def cadastrar_profissional(dados: ProfissionalCreate, db: Session = Depends(get_db)):
    try:
        return profissonal_service.cria_profissional(db, dados)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
@router.put('/{profissional_id}')
def atualizar_profissional(profissional_id: int, dados: ProfissionalUpdate, db: Session = Depends(get_db)):
    try: 
        profissional = profissonal_service.atualizar_profissional(db, dados, profissional_id)
        return profissional
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
@router.get('/')
def listar_profissionais(db: Session = Depends(get_db)):
    return profissonal_service.listar_profissionais(db)
@router.delete('/{profissional_id}')
def deletar_profissional(profissional_id: int, db: Session = Depends(get_db)):
    try:
        return profissonal_service.deletar_profissional(db, profissional_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))