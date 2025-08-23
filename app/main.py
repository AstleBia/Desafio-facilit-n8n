from fastapi import FastAPI
from app.routers import agenda_rh
app = FastAPI()
app.include_router(agenda_rh.routes)

@app.get("/")
async def root():
    return {"message": "Hello World"}
