from database.conexao import Base, engine
from models import paciente, profissional, agendamento, atendimento

#Rodar essa aplicação: python -m Scripts.create_table
# Criando as tabelas 
def db_init():
    Base.metadata.create_all(bind=engine)
db_init()