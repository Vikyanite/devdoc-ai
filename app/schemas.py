
from pydantic import BaseModel

class ChatMessage(BaseModel):
    role : str
    content : str

class ChatRequest(BaseModel):
    user_id : str
    message : str
    history : list[ChatMessage] = []  # 指定元素类型，并提供默认值

class ChatResponse(BaseModel):
    answer : str