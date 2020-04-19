from app.api import token, vehicles, messages
from app.db import database, engine, metadata, migrate
from fastapi import FastAPI
from starlette.responses import RedirectResponse

metadata.create_all(engine)

app = FastAPI()


@app.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse(url="/docs")


@app.on_event("startup")
async def startup():
    await database.connect()
    await migrate()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(token.router)
app.include_router(vehicles.router)
app.include_router(messages.router)
