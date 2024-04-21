from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class FinanceAccountResponse(BaseModel):
    id: UUID
    name: str
    iban: str
    balance: float
    currency: str
    created_at: datetime
    updated_at: datetime

    class Config:
        ignore_extra = True
