from dataclasses import dataclass

from sqlalchemy import Column, String, Boolean, DateTime, Text, SmallInteger
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import Mapped
from sqlalchemy.dialects.postgresql import JSON

from v1.clients.postgres import SyncBase


@dataclass
class User(SyncBase):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    instance_id: Mapped[UUID] = Column(UUID, primary_key=True)
    id: Mapped[UUID] = Column(UUID)
    aud: Mapped[str] = Column(String)
    role: Mapped[str] = Column(String)
    email: Mapped[str] = Column(String)
    encrypted_password: Mapped[str] = Column(String)
    email_confirmed_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    invited_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    confirmation_token: Mapped[str] = Column(String)
    confirmation_sent_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    recovery_token: Mapped[str] = Column(String)
    recovery_sent_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    email_change_token_new: Mapped[str] = Column(String)
    email_change: Mapped[str] = Column(String)
    email_change_sent_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    last_sign_in_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    raw_app_meta_data: Mapped[JSON] = Column(JSON)
    raw_user_meta_data: Mapped[JSON] = Column(JSON)
    is_super_admin: Mapped[bool] = Column(Boolean)
    created_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    updated_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    phone: Mapped[str] = Column(Text)
    phone_confirmed_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    phone_change: Mapped[str] = Column(Text)
    phone_change_token: Mapped[str] = Column(String)
    phone_change_sent_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    confirmed_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    email_change_token_current: Mapped[str] = Column(String)
    email_change_confirm_status: Mapped[int] = Column(SmallInteger)
    banned_until: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    reauthentication_token: Mapped[str] = Column(String)
    reauthentication_sent_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    is_sso_user: Mapped[bool] = Column(Boolean)
    deleted_at: Mapped[DateTime] = Column(TIMESTAMP(timezone=True))
    is_anonymous: Mapped[bool] = Column(Boolean)
