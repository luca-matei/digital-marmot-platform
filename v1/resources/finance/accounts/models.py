from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    String,
    text,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped

from v1.clients.postgres import SyncBase


@dataclass
class FinanceAccount(SyncBase):
    __tablename__ = 'finance_accounts'

    id: Mapped[UUID] = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    created_at: Mapped[datetime] = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at: Mapped[datetime] = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )
    user_id: Mapped[UUID] = Column(
        UUID(as_uuid=True),
        ForeignKey("auth.users.id", ondelete="CASCADE"),
        nullable=False
    )
    name: Mapped[str] = Column(String, nullable=False)
    iban: Mapped[str] = Column(String, nullable=False)
    currency: Mapped[str] = Column(String, nullable=False)
