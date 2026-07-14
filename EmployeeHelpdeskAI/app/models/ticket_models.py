from pydantic import BaseModel


class TicketClassification(BaseModel):

    department: str

    category: str

    priority: str

    summary: str