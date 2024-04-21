from fastapi import APIRouter

from v1.clients.postgres import PostgresSession
from v1.resources.finance.accounts.models import FinanceAccount
from v1.resources.finance.accounts.schemas import FinanceAccountResponse

router = APIRouter(prefix="/accounts")


@router.get("")
async def get_accounts():
    with PostgresSession() as session:
        accounts = session.query(FinanceAccount).all()
        accounts = [FinanceAccountResponse(**a.__dict__) for a in accounts]

    return {
        "accounts": accounts,
        "count": len(accounts),
    }


@router.post("")
async def create_account():
    pass


@router.put("/{account_id}")
async def update_account(account_id: int):
    pass


@router.delete("/{account_id}")
async def delete_account(account_id: int):
    pass
