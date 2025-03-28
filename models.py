from pydantic import BaseModel
from typing import List, Dict

class MessageModel(BaseModel):
    sender: str
    message: str
    timestamp: str

class ChatModel(BaseModel):
    conversation_id: str
    user_id: str
    messages: List[MessageModel]
