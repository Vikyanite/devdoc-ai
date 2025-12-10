import httpx
from fastapi import FastAPI, HTTPException
from .schemas import ChatResponse, ChatRequest, ChatMessage
from .llm_client import llm_client

app = FastAPI(title="DevDoc AI Assistant", version="0.0.1")

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        history = req.history or []

        # 1. system 消息：设定角色
        messages = []
        # 2. 历史消息（可能是 user/assistant 混合）
        messages.extend(history)
        # 3. 当前用户消息
        messages.append(ChatMessage(role="user", content=req.message))

        answer = await llm_client.chat(messages)

        return ChatResponse(answer=answer)
    except (httpx.ReadTimeout, httpx.ConnectTimeout) as e:
        # 特殊处理 timeout 异常，返回 504 Gateway Timeout
        raise HTTPException(status_code=504, detail=f"LLM API 请求超时：{str(e)}")
    except Exception as e:
        # 这里简单处理，实际可以打日志再包装错误
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ping")
async def ping():
    return {"msg": "pong"}
