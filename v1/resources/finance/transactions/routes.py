from uuid import UUID

from fastapi import APIRouter

from v1.clients.postgres import PostgresSession
from v1.resources.finance.accounts.models import FinanceAccount
from v1.resources.finance.transactions.models import FinanceTransaction
from v1.resources.finance.transactions.schemas import FinanceTransactionResponse

router = APIRouter(prefix="/transactions")


@router.get("")
async def get_transactions(
    account_id: UUID = None,
    filters: str = None,
    sort: str = None,
    offset: int = 0,
    limit: int = 10,
):
    with PostgresSession() as session:
        transactions = session.query(FinanceTransaction).limit(limit).offset(offset).all()
        transactions = [FinanceTransactionResponse(**t.__dict__) for t in transactions]

        if filters:
            total_count = session.query(FinanceAccount).filter_by(id=account_id).first().transactions_count
        else:
            total_count = session.query(FinanceAccount).filter_by(id=account_id).first().transactions_count

    return {
        "transactions": transactions,
        "count": len(transactions),
        "total": total_count,
    }


@router.post("")
async def create_transaction():
    pass


@router.put("/{transaction_id}")
async def update_transaction(transaction_id: int):
    pass


@router.delete("/{transaction_id}")
async def delete_transaction(transaction_id: int):
    pass
