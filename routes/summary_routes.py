from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from database import chats_collection
from services.summarization import generate_summary

router = APIRouter()

class ChatRequest(BaseModel):
    conversation_id: str

@router.post("/chats/summarize")
def summarize_chat(request: ChatRequest):
    print("hi")
    chat = chats_collection.find_one({"conversation_id": request.conversation_id})
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    summary = generate_summary(chat)
    return {"conversation_id": request.conversation_id, "summary": summary}

@router.get("/{user_id}/chats")
async def get_user_chats(user_id: str, page: int = 1, limit: int = 10):
    skip = (page - 1) * limit
    chats_cursor = chats_collection.find({"user_id": user_id}).skip(skip).limit(limit)

    chats = []
    for chat in chats_cursor:
        chat["_id"] = str(chat["_id"])
        chats.append(chat)

    return {"page": page, "limit": limit, "data": chats}
