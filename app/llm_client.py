import httpx

from app.schemas import ChatMessage
from .config import settings

class LLMClient:
    def __init__(self):
        self.api_key = settings.LLM_API_KEY
        self.base_url = settings.LLM_BASE_URL
        self.model = settings.LLM_MODEL

    async def chat(self, messages: list[ChatMessage]) -> str:
        payload = {
            "model": self.model,
            "messages": [m.model_dump() for m in messages],
        }
        timeout = httpx.Timeout(
            connect=5.0,  # 建立连接最多等 5 秒
            read=40.0,  # 读取响应最多等 40 秒（LLM 主耗时）
            write=10.0,  # 发送请求最多 10 秒
            pool=5.0,  # 连接池相关，这里随便给个值就行
        )
        async with httpx.AsyncClient(base_url=self.base_url, headers={
            "Authorization": f"Bearer {self.api_key}"
        }, timeout=timeout) as client:
            resp = await client.post("/chat/completions", json=payload)
            resp.raise_for_status()
            data = resp.json()
        try:
            ret = data["choices"][0]["message"]["content"]
            return ret
        except KeyError:
            return data["error"]["message"]


llm_client = LLMClient()