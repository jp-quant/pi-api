import pandas as pd
from datetime import datetime, timedelta
from models import AnalyticsData
import data_manager
import config



def get_lowest_price(data, ticket_source, ticket_date, time_delta):
    filtered_data = data[(data['ticket_source'] == ticket_source) &
                         (data['ticket_date'] == ticket_date) &
                         (pd.to_datetime(data['timestamp']) >= (datetime.now() - time_delta))]
    return filtered_data['ticket_price'].min()

def compile_analytics_report():
    data = data_manager.read_data()()
    analytics_results = []

    for ticket_source in ['vividseats', 'seatgeek']:
        for ticket_date in config.TICKET_DATES:
            last_hour_lowest_price = get_lowest_price(data, ticket_source, ticket_date, timedelta(hours=1))
            last_day_lowest_price = get_lowest_price(data, ticket_source, ticket_date, timedelta(days=1))
            last_week_lowest_price = get_lowest_price(data, ticket_source, ticket_date, timedelta(weeks=1))

            analytics_data = AnalyticsData(
                timestamp=datetime.now(),
                ticket_source=ticket_source,
                ticket_date=ticket_date,
                last_hour_lowest_price=last_hour_lowest_price,
                last_day_lowest_price=last_day_lowest_price,
                last_week_lowest_price=last_week_lowest_price
            )

            analytics_results.append(analytics_data)

    return analytics_results

