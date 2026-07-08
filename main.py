from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from config import EXTERNAL_RECOMMENDATIONS_URL

app = FastAPI()

class RecommendationRequest(BaseModel):
    category: str | None = None

class RecommendationItem(BaseModel):
    id: int
    title: str
    body: str

@app.post("/recommendations", response_model=list[RecommendationItem])
def get_recommendations(req: RecommendationRequest):
    demo_items = [
        {
            "id": 1,
            "title": "Наушники беспроводные с шумоподавлением",
            "body": "Стильные и лёгкие, работают до 30 часов без подзарядки…"
        },
        {
            "id": 2,
            "title": "Умная колонка с голосовым помощником",
            "body": "Компактная колонка, которая управляет умным домом…"
        },
        {
            "id": 3,
            "title": "Фитнес‑браслет с мониторингом сна и стресса",
            "body": "Лёгкий и удобный браслет отслеживает шаги, пульс…"
        }
    ]
    return demo_items
