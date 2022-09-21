import time

from fastapi import FastAPI, Request

from app.routers import router

app = FastAPI(
    title="MyApp",
    description=("My First App using fastapi"),
    version="0.0.1",
    docs_url="/doc",
    redoc_url="/doc/redoc",
)
app.include_router(router)