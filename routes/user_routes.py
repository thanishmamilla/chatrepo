from fastapi import APIRouter, Query
from database import chats_collection

router = APIRouter()

# ✅ Get User's Chat History (Paginated)
@router.get("/{user_id}/chats")
async def get_user_chats(user_id: str, page: int = 1, limit: int = 10):
    skip = (page - 1) * limit
    chats_cursor = chats_collection.find({"user_id": user_id}).skip(skip).limit(limit)

    chats = []
    for chat in chats_cursor:
        chat["_id"] = str(chat["_id"])
        chats.append(chat)

    return {"page": page, "limit": limit, "data": chats}
