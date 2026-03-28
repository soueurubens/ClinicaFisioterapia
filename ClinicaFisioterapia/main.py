from fastapi import FastAPI
from routers.paciente_router import router as paciente_router
from routers.profissional_router import router as profissional_router

# Rodar a API --> python -m uvicorn main:app --reload


app = FastAPI()
app.include_router(paciente_router)
app.include_router(profissional_router)

