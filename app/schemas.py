from pydantic import BaseModel, Field
from typing import Literal


Category = Literal[
    "Delivery Issue",
    "Billing",
    "Product Quality",
    "Technical Issue",
    "General"
]

Urgency = Literal["Low", "Medium", "High"]


class TicketRequest(BaseModel):
    message: str = Field(..., min_length=5)


class TicketClassification(BaseModel):
    category: Category
    urgency: Urgency
    summary: str
    recommended_action: str