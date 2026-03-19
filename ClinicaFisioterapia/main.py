from fastapi import FastAPI
from routers.paciente_router import router as paciente_router

# Rodar a API --> python -m uvicorn main:app --reload


app = FastAPI()
app.include_router(paciente_router)

