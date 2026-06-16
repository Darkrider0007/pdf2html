from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.pdf_routes import router

app = FastAPI()

app.include_router(router)

app.mount(
    "/output",
    StaticFiles(directory="output"),
    name="output"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)