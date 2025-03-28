from fastapi import APIRouter, HTTPException
from database import chats_collection
from models import ChatModel
from typing import List

router = APIRouter()

# ✅ Store a Single Chat
@router.post("/")
async def store_chat(chat: ChatModel):
    chat_dict = chat.model_dump()  # Pydantic v2 (use `.dict()` for Pydantic v1)
    result = chats_collection.insert_one(chat_dict)
    return {"message": "Chat stored successfully", "id": str(result.inserted_id)}

# ✅ Bulk Insert Chats
@router.post("/bulk")
async def store_bulk_chats(chats: List[ChatModel]):
    chat_dicts = [chat.dict() for chat in chats]
    result = chats_collection.insert_many(chat_dicts)
    return {"message": "Bulk chats stored", "inserted_ids": [str(id) for id in result.inserted_ids]}

# ✅ Retrieve Chat by ID
@router.get("/{conversation_id}")
async def get_chat(conversation_id: str):
    chat = chats_collection.find_one({"conversation_id": conversation_id})
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    chat["_id"] = str(chat["_id"])
    return chat

# ✅ Soft Delete a Chat
@router.delete("/{conversation_id}")
async def soft_delete_chat(conversation_id: str):
    result = chats_collection.update_one(
        {"conversation_id": conversation_id}, {"$set": {"deleted": True}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Chat not found")
    return {"message": "Chat marked as deleted"}
