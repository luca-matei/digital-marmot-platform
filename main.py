import uvicorn

from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from v1.config import settings
from v1.resources.weather.routes import router as weather_router
from v1.resources.finance.routes import router as finance_router

app = FastAPI()
router = APIRouter(prefix="/v1")


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

router.include_router(weather_router)
router.include_router(finance_router)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.host_ip, port=settings.host_port, reload=True)
