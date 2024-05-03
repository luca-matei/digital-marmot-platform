from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class NoteTreeResponse(BaseModel):
    id: UUID
    title: str
    icon: Optional[str]
    parent_id: Optional[UUID]
    order: int


class NoteResponse(NoteTreeResponse):
    created_at: datetime
    updated_at: datetime
