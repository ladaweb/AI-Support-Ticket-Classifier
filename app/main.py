from fastapi import FastAPI
from app.schemas import TicketRequest, TicketClassification
from app.ai_service import classify_ticket

app = FastAPI(title="AI Support Ticket Classifier")


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "AI Ticket Classifier is running"
    }


@app.post("/classify", response_model=TicketClassification)
def classify(request: TicketRequest):
    return classify_ticket(request.message)
