from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.routes.pdf_routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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