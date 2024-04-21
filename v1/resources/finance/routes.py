from fastapi import APIRouter

from v1.resources.finance.transactions.routes import router as transactions_router

router = APIRouter(prefix="/finance")

router.include_router(transactions_router)
