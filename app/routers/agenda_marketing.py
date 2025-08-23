from fastapi import APIRouter, HTTPException
from app.schema import EventoMarketingCreate
from app.database import SessionDep
from app.models import EventoMarketing
from sqlmodel import select

router = APIRouter()

@router.get("/eventos-marketing", response_model=list[EventoMarketing])
def read_eventos(session:SessionDep) -> list[EventoMarketing]:
    eventos  = session.exec(select(EventoMarketing)).all()
    return eventos

@router.get("/eventos-marketing/{evento_id}", response_model = EventoMarketing)
def read_evento(evento_id:int, session:SessionDep) -> EventoMarketing:
    evento = session.get(EventoMarketing, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return evento

@router.post("/eventos-marketing", response_model=EventoMarketing)
def create_evento(evento:EventoMarketingCreate, session:SessionDep) -> EventoMarketing:
    new_evento = EventoMarketing(data_inicio = evento.data_inicio, data_fim = evento.data_fim, evento = evento.evento, descricao = evento.descricao, status = evento.status.value)
    session.add(new_evento)
    session.commit()
    session.refresh(new_evento)
    return new_evento

@router.put("/eventos-marketing/{evento_id}", response_model= EventoMarketing)
def update_evento(evento_id:int, evento_updated: EventoMarketingCreate, session:SessionDep) -> EventoMarketing:
    evento = session.get(EventoMarketing, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    evento.data_inicio = evento_updated.data_inicio
    evento.data_fim = evento_updated.data_fim
    evento.evento = evento_updated.evento
    evento.descricao = evento_updated.descricao
    evento.status.value = evento_updated.status
    session.add(evento)
    session.commit()
    session.refresh(evento)
    return evento

@router.delete("/eventos-marketing/{evento_id}", response_model=EventoMarketing)
def delete_evento(evento_id:int, session:SessionDep) -> EventoMarketing:
    evento = session.get(EventoMarketing, evento_id)
    if not evento:
        raise HTTPException (status_code=404, detail="Evento não encontrado")
    session.delete(evento)
    session.commit()
    return evento