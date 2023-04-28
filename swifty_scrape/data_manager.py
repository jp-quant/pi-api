import pandas as pd
from models import TicketData, AnalyticsData
import os

CSV_FILE = "ticket_data.csv"

def read_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=["timestamp", "ticket_price", "ticket_source", "ticket_date"])

def write_data(data):
    data.to_csv(CSV_FILE, index=False)

def update_data(new_data: TicketData):
    data = read_data()
    data = data.append(new_data.dict(), ignore_index=True)
    write_data(data)




ANALYTICS_CSV_FILE = "analytics_data.csv"

def read_analytics_data():
    if os.path.exists(ANALYTICS_CSV_FILE):
        return pd.read_csv(ANALYTICS_CSV_FILE)
    else:
        return pd.DataFrame(columns=["timestamp", "ticket_source", "ticket_date", "last_hour_lowest_price", "last_day_lowest_price", "last_week_lowest_price"])

def update_analytics_data(analytics_data: AnalyticsData):
    data = read_analytics_data()
    data = data.append(analytics_data.dict(), ignore_index=True)
    data.to_csv(ANALYTICS_CSV_FILE, index=False)