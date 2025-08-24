from pydantic import BaseModel

class EventoRhCreate(BaseModel):
    data_anual:str
    evento:str
    descricao:str
    alcance:int
    status:str

class EventoMarketingCreate(BaseModel):
    data_anual:str
    evento:str
    descricao:str
    status:str

class EventoIACreate(BaseModel):
    data_anual:str
    evento:str
    descricao:str
    engajamento:int
    status:str