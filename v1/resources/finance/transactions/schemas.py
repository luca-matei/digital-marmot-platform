from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class FinanceTransactionResponse(BaseModel):
    id: UUID
    amount: Decimal
    category: str
    title: str
    description: Optional[str]
    account_id: UUID
    timestamp: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        ignore_extra = True
