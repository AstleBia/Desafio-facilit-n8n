from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine
import os
from dotenv import load_dotenv

load_dotenv()


database_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/desafio"
connect_args = {"check_same_thread": False}
engine = create_engine(database_url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]