import uvicorn

from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from v1.config import settings
from v1.resources.weather.routes import router as weather_router

app = FastAPI()
router = APIRouter()


@app.get("/")
def root():
    return RedirectResponse(url="/v1")


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/health")
async def health():
    return {"status": "ok"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather_router, prefix="/v1")
app.include_router(router, prefix="/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.host_ip, port=settings.host_port, reload=True)
