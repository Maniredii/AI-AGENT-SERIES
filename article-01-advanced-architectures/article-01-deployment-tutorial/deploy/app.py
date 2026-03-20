from fastapi import FastAPI
from pydantic import BaseModel
from crew import run_crew

app = FastAPI(title="MCP-Powered Market Analyst API")

class AnalysisRequest(BaseModel):
    topic: str

@app.post("/analyze")
async def analyze(req: AnalysisRequest):
    result = run_crew(req.topic)
    return {"report": str(result)}

@app.get("/health")
async def health():
    return {"status": "ok"}
