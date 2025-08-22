from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine, Field, Column, Enum
from datetime import date
import enum
import os
from dotenv import load_dotenv

load_dotenv()

class Status (str, enum.Enum):
    NaoIniciado = "Não iniciado"
    EmAndamento = "Em andamento"
    Concluido = "Concluído"

class AgendaRh(SQLModel, table=True):
    id:int = Field(primary_key=True)
    data_inicio:date
    data_fim:date
    evento:str = Field(max_length=100)
    descricao:str
    alcance:int
    status:Status = Field(sa_column=Column(Enum(Status, name="status", create_type = False)))

class AgendaMarketing(SQLModel, table = True):
    id: int = Field(primary_key=True)
    data_inicio: date
    data_fim: date
    evento: str = Field(max_length=100)
    descricao: str
    status: Status = Field(sa_column=Column(Enum(Status, name="status", create_type=False)))

class AgendaIA(SQLModel, table = True):
    id:int = Field(primary_key=True)
    data_inicio:date
    data_fim:date
    evento:str = Field(max_length=100)
    descricao:str
    engajamento:int
    status: Status = Field(sa_column=Column(Enum(Status, name="status", create_type=False)))

database_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/desafio"
connect_args = {"check_same_thread": False}
engine = create_engine(database_url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]