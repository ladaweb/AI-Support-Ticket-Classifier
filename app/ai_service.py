import json
import os
import requests
from dotenv import load_dotenv
from app.schemas import TicketClassification

load_dotenv()

USE_MOCK = os.getenv("USE_MOCK", "true").lower() == "true"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")


def mock_classify_ticket(message: str) -> TicketClassification:
    text = message.lower()

    if "charged" in text or "refund" in text or "payment" in text or "twice" in text:
        category = "Billing"
        urgency = "High"
        action = "Route to billing support and check payment/refund history."
    elif "cold" in text or "wrong" in text or "missing" in text or "burnt" in text:
        category = "Product Quality"
        urgency = "Medium"
        action = "Route to store/customer care for order quality review."
    elif "app" in text or "website" in text or "login" in text or "crash" in text:
        category = "Technical Issue"
        urgency = "Medium"
        action = "Route to technical support and collect device/app details."
    elif "late" in text or "driver" in text or "never arrived" in text or "delivery" in text:
        category = "Delivery Issue"
        urgency = "High"
        action = "Route to delivery support and review order tracking."
    else:
        category = "General"
        urgency = "Low"
        action = "Route to general support queue."

    return TicketClassification(
        category=category,
        urgency=urgency,
        summary=f"Customer issue: {message[:120]}",
        recommended_action=action
    )


def build_prompt(message: str) -> str:
    return f"""
You are an AI support ticket classifier for a pizza delivery company.

Your task:
Convert the customer's message into structured JSON.

Allowed categories:
- Delivery Issue
- Billing
- Product Quality
- Technical Issue
- General

Allowed urgency levels:
- Low
- Medium
- High

Return ONLY valid JSON.
Do not include markdown.
Do not include explanations.

JSON format:
{{
  "category": "...",
  "urgency": "...",
  "summary": "...",
  "recommended_action": "..."
}}

Customer message:
{message}
"""


def classify_with_ollama(message: str) -> TicketClassification:
    prompt = build_prompt(message)

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()

        raw_response = response.json()["response"]

        parsed = json.loads(raw_response)

        return TicketClassification(**parsed)

    except Exception as error:
        print(f"Ollama classification failed. Falling back to mock classifier. Error: {error}")
        return mock_classify_ticket(message)


def classify_ticket(message: str) -> TicketClassification:
    if USE_MOCK:
        return mock_classify_ticket(message)

    return classify_with_ollama(message)