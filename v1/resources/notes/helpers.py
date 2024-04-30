from uuid import UUID

from v1.clients.postgres import PostgresSession
from v1.resources.notes.models import NotesFile
from v1.resources.notes.schemas import NoteTreeResponse


def create_note(user_id: UUID, parent_id: UUID = None):
    with PostgresSession() as session:
        note = NotesFile(
            parent_id=parent_id,
            title="Untitled",
            user_id=user_id,
        )
        session.add(note)
        return note.id


def get_tree(user_id: UUID, parent_id: UUID = None):
    with PostgresSession() as session:
        note_tree = (
            session.query(NotesFile)
            .filter(NotesFile.parent_id == parent_id, NotesFile.user_id == user_id)
            .all()
        )
        note_tree = [NoteTreeResponse(**nt.__dict__) for nt in note_tree]
        return note_tree


def delete_note(note_id: UUID):
    with PostgresSession() as session:
        note = session.query(NotesFile).get(note_id)
        if not note:
            return False
        session.delete(note)
        return True
