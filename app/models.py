from sqlmodel import SQLModel, Field

class EventoRh(SQLModel, table=True):
    __tablename__ = "agenda_rh"
    id:int = Field(primary_key=True)
    data_anual:str = Field(max_length=50)
    evento:str = Field(max_length=100)
    descricao:str
    alcance:int
    status:str = Field(max_length=50)

class EventoMarketing(SQLModel, table = True):
    __tablename__ = "agenda_marketing"
    id: int = Field(primary_key=True)
    data_anual:str = Field(max_length=50)
    evento: str = Field(max_length=100)
    descricao: str
    status:str = Field(max_length=50)

class EventoIA(SQLModel, table = True):
    __tablename__ = "agenda_ia"
    id:int = Field(primary_key=True)
    data_anual:str = Field(max_length=50)
    evento:str = Field(max_length=100)
    descricao:str
    engajamento:int
    status:str = Field(max_length=50)