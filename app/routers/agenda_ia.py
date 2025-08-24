from fastapi import APIRouter, HTTPException
from app.schema import EventoIACreate
from app.database import SessionDep
from app.models import EventoIA
from sqlmodel import select

router = APIRouter()

@router.get("/eventos-ia", response_model=list[EventoIA])
def read_eventos(session:SessionDep) -> list[EventoIA]:
    eventos  = session.exec(select(EventoIA)).all()
    return eventos

@router.get("/eventos-ia/{evento_id}", response_model = EventoIA)
def read_evento(evento_id:int, session:SessionDep) -> EventoIA:
    evento = session.get(EventoIA, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return evento

@router.post("/eventos-ia", response_model=EventoIA)
def create_evento(evento:EventoIACreate, session:SessionDep) -> EventoIA:
    new_evento = EventoIA(data_anual = evento.data_anual, evento = evento.evento, descricao = evento.descricao, engajamento = evento.engajamento, status = evento.status)
    session.add(new_evento)
    session.commit()
    session.refresh(new_evento)
    return new_evento

@router.put("/eventos-ia/{evento_id}", response_model= EventoIA)
def update_evento(evento_id:int, evento_updated: EventoIACreate, session:SessionDep) -> EventoIA:
    evento = session.get(EventoIA, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    evento.data_anual = evento_updated.data_anual
    evento.evento = evento_updated.evento
    evento.descricao = evento_updated.descricao
    evento.engajamento = evento_updated.engajamento
    evento.status = evento_updated.status
    session.add(evento)
    session.commit()
    session.refresh(evento)
    return evento

@router.delete("/eventos-ia/{evento_id}", response_model=EventoIA)
def delete_evento(evento_id:int, session:SessionDep) -> EventoIA:
    evento = session.get(EventoIA, evento_id)
    if not evento:
        raise HTTPException (status_code=404, detail="Evento não encontrado")
    session.delete(evento)
    session.commit()
    return evento