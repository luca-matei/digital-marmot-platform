from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class NoteTreeResponse(BaseModel):
    id: UUID
    title: str
    icon: Optional[str]
