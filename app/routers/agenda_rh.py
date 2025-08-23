from fastapi import APIRouter, HTTPException
from app.schema import EventoRhCreate
from app.database import SessionDep
from app.models import EventoRh
from sqlmodel import select

router = APIRouter()

@router.get("/eventos-rh", response_model=list[EventoRh])
def read_eventos(session:SessionDep) -> list[EventoRh]:
    eventos  = session.exec(select(EventoRh)).all()
    return eventos

@router.get("/eventos-rh/{evento_id}", response_model = EventoRh)
def read_evento(evento_id:int, session:SessionDep) -> EventoRh:
    evento = session.get(EventoRh, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return evento

@router.post("/eventos-rh", response_model=EventoRh)
def create_evento(evento:EventoRhCreate, session:SessionDep) -> EventoRh:
    new_evento = EventoRh(data_inicio = evento.data_inicio, data_fim = evento.data_fim, evento = evento.evento, descricao = evento.descricao, alcance = evento.alcance, status = evento.status.value)
    session.add(new_evento)
    session.commit()
    session.refresh(new_evento)
    return new_evento

@router.put("/eventos-rh/{evento_id}", response_model= EventoRh)
def update_evento(evento_id:int, evento_updated: EventoRhCreate, session:SessionDep) -> EventoRh:
    evento = session.get(EventoRh, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    evento.data_inicio = evento_updated.data_inicio
    evento.data_fim = evento_updated.data_fim
    evento.evento = evento_updated.evento
    evento.descricao = evento_updated.descricao
    evento.alcance = evento_updated.alcance
    evento.status = evento_updated.status.value
    session.add(evento)
    session.commit()
    session.refresh(evento)
    return evento

@router.delete("/eventos-rh/{evento_id}", response_model=EventoRh)
def delete_evento(evento_id:int, session:SessionDep) -> EventoRh:
    evento = session.get(EventoRh, evento_id)
    if not evento:
        raise HTTPException (status_code=404, detail="Evento não encontrado")
    session.delete(evento)
    session.commit()
    return evento



