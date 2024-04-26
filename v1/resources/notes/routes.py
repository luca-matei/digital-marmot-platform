from uuid import UUID

from fastapi import APIRouter
from starlette.requests import Request

from v1.resources.notes.helpers import create_note, get_tree, delete_note

router = APIRouter(prefix="/notes")


@router.get("/tree")
async def get_root_note_tree(request: Request):
    note_tree = get_tree(request.state.user_id)
    return {"tree": note_tree}


@router.get("/tree/{note_id}")
async def get_note_tree(request: Request, note_id: UUID):
    note_tree = get_tree(request.state.user_id, note_id)
    return {"tree": note_tree}


@router.get("")
async def get_notes():
    pass


@router.post("")
async def create_root_note(request: Request):
    new_note_id = create_note(request.state.user_id)
    return {"id": new_note_id}


@router.post("/{note_id}")
async def create_child_note(request: Request, note_id: UUID):
    new_note_id = create_note(request.state.user_id, note_id)
    return {"id": new_note_id}


@router.put("/{note_id}")
async def update_note(note_id: UUID):
    pass


@router.delete("/{note_id}")
async def delete_note_route(request: Request, note_id: UUID):
    deleted = delete_note(note_id)
    return {"deleted": deleted}
