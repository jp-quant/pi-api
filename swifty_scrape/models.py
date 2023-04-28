from pydantic import BaseModel
from datetime import datetime

class TicketData(BaseModel):
    timestamp: datetime
    ticket_price: float
    ticket_source: str
    ticket_date: str

class AnalyticsData(BaseModel):
    timestamp: datetime
    ticket_source: str
    ticket_date: str
    last_hour_lowest_price: float
    last_day_lowest_price: float
    last_week_lowest_price: float


# Add any additional validation or data processing here if needed
