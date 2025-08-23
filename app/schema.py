from pydantic import BaseModel
from datetime import date
import enum
from models import Status

class AgendaRh(BaseModel):
    id:int
    data_inicio:date
    data_fim:date
    evento:str
    descricao:str
    alcance:int
    status:Status

class AgendaMarketing(BaseModel):
    id:int
    data_inicio:date
    data_fim:date
    evento:str
    descricao:str
    status:Status

class AgendaIA(BaseModel):
    id:int
    data_inicio:date
    data_fim:date
    evento:str
    descricao:str
    engajamento:int
    status:Status