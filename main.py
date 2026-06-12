from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone

app = FastAPI(
    title="Interstellar Complex Exploration System",
    description="Genesis Node - Year 0",
    version="1.0.0"
)

class Telemetry(BaseModel):
    sector: str
    status: str
    timestamp: str

@app.get("/")
async def system_status():
    return {
        "directive": "Survive and Explore",
        "uptime_epoch": datetime.now(timezone.utc).isoformat(),
        "systems": "Nominal"
    }

@app.post("/telemetry/log")
async def log_telemetry(data: Telemetry):
    if not data:
        raise HTTPException(status_code=400, detail="No telemetry data received.")
    
    # In a production state, this routes to a document-based store
    return {"status": "recorded", "data": data}