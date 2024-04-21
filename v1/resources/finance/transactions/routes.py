from fastapi import APIRouter

from v1.clients.postgres import PostgresSession
from v1.resources.finance.transactions.models import FinanceTransaction

router = APIRouter(prefix="/transactions")


@router.get("")
async def get_transactions():
    with PostgresSession() as session:
        transactions = session.query(FinanceTransaction).all()
        return transactions


@router.post("")
async def create_transaction():
    pass


@router.put("/{transaction_id}")
async def update_transaction(transaction_id: int):
    pass


@router.delete("/{transaction_id}")
async def delete_transaction(transaction_id: int):
    pass
