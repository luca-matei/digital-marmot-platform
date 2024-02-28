# Main FastAPI application

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/version")
async def version():
    return {"version": settings.version}


@app.get("/info")
async def info():
    return {
        "name": "Digital Marmot Platform API",
        "description": "API for the Digital Marmot Platform",
        "version": settings.version,
        "author": "Luca Matei",
        "email": "dev@lucamatei.eu",
        "license": "MIT",
        "website": "https://lucamatei.eu",
        "repository": "https://github.com/luca-matei/digital-marmot-platform",
    }
