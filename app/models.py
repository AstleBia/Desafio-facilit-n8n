from sqlmodel import SQLModel, Field, Column, Enum
from datetime import date
import enum


class Status (str, enum.Enum):
    nao_iniciado = "nao_iniciado"
    em_andamento = "em_andamento"
    concluido = "concluido"

class EventoRh(SQLModel, table=True):
    __tablename__ = "agenda_rh"
    id:int = Field(primary_key=True)
    data_inicio:date
    data_fim:date
    evento:str = Field(max_length=100)
    descricao:str
    alcance:int
    status:Status = Field(sa_column=Column(Enum(Status, name="status", create_type = False)))

class EventoMarketing(SQLModel, table = True):
    __tablename__ = "agenda_marketing"
    id: int = Field(primary_key=True)
    data_inicio: date
    data_fim: date
    evento: str = Field(max_length=100)
    descricao: str
    status: Status = Field(sa_column=Column(Enum(Status, name="status", create_type=False)))

class EventoIA(SQLModel, table = True):
    __tablename__ = "agenda_ia"
    id:int = Field(primary_key=True)
    data_inicio:date
    data_fim:date
    evento:str = Field(max_length=100)
    descricao:str
    engajamento:int
    status: Status = Field(sa_column=Column(Enum(Status, name="status", create_type=False)))