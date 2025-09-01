from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from serpapi import GoogleSearch
import uvicorn

load_dotenv()
app = FastAPI()

class ChatRequest(BaseModel):
    messages: list
    stream: bool = False
    search: bool = False

async def search_web(query: str):
    params = {
        "q": query,
        "api_key": "13d7b48bf7f3c01369a57e7e602c46fdb0e55e42412d67704c1cd99a76e21453",
        "engine": "google",
        "num": 3
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    snippets = []
    for r in results.get("organic_results", []):
        if "snippet" in r:
            snippets.append(r["snippet"])
    return "\n".join(snippets)

@app.post("/mcp/chat")
async def mcp_chat(req: ChatRequest):
    messages = req.messages
    if messages:
        # 默认对最后一条用户消息执行搜索
        user_msg = messages[-1].get("content", "")
        web_content = await search_web(user_msg)
        messages.append({
            "role": "system",
            "content": f"以下是最新互联网搜索结果：\n{web_content}"
        })
        print("=====messages=====")
        print(messages)
        return messages
    
if __name__ == "__main__":    
    uvicorn.run(app, host="0.0.0.0", port=6666)
