from fastapi import APIRouter

from v1.resources.finance.transactions.routes import router as transactions_router
from v1.resources.finance.accounts.routes import router as accounts_router

router = APIRouter(prefix="/finance")

router.include_router(transactions_router)
router.include_router(accounts_router)
