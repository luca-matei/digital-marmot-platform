from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Column, DateTime, String, Text, ForeignKey, text, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped

from v1.clients.postgres import SyncBase


@dataclass
class NotesFile(SyncBase):
    __tablename__ = "notes_files"

    # UUID for the note file; generated automatically
    id: Mapped[UUID] = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )

    # Automatic timestamps for when notes are created and updated
    created_at: Mapped[datetime] = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
    updated_at: Mapped[datetime] = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    # Optional UUID for a parent note, if any
    parent_id: Mapped[UUID] = Column(
        UUID(as_uuid=True),
        ForeignKey("notes_files.id", ondelete="SET NULL"),
        nullable=True,
    )

    # Icon for the note (optional)
    icon: Mapped[str] = Column(String, nullable=True)

    # Title of the note file
    title: Mapped[str] = Column(String, nullable=False)

    # Link to user's ID
    user_id: Mapped[UUID] = Column(
        UUID(as_uuid=True),
        ForeignKey("user_profiles.id", ondelete="CASCADE"),
        nullable=False,
    )

    order: Mapped[int] = Column(Integer, nullable=False)


@dataclass
class UserProfile(SyncBase):
    __tablename__ = "user_profiles"

    id: Mapped[UUID] = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )

    created_at: Mapped[datetime] = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
    updated_at: Mapped[datetime] = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    # User's email address
    full_name: Mapped[str] = Column(String, nullable=False)

    # User's hashed password
    username: Mapped[str] = Column(String, nullable=False)
