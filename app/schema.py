from pydantic import BaseModel
from datetime import date
from app.models import Status

class EventoRhCreate(BaseModel):
    data_inicio:date
    data_fim:date
    evento:str
    descricao:str
    alcance:int
    status:Status

class EventoMarketingCreate(BaseModel):
    data_inicio:date
    data_fim:date
    evento:str
    descricao:str
    status:Status

class EventoIACreate(BaseModel):
    data_inicio:date
    data_fim:date
    evento:str
    descricao:str
    engajamento:int
    status:Status