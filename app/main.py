from fastapi import FastAPI
from app.routers import agenda_rh,agenda_marketing,agenda_ia
app = FastAPI()
app.include_router(agenda_rh.router)
app.include_router(agenda_marketing.router)
app.include_router(agenda_ia.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
