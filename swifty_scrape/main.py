import time
import config
import scraper
import data_manager
import analytics
import emailer
from models import TicketData
from datetime import datetime, timedelta

def main():
    while True:
        # Scrape data
        for date in config.TICKET_DATES:
            vividseats_data = scraper.scrape_vividseats(date)
            seatgeak_data = scraper.scrape_seatgeak(date)
            
            # Update data
            for data in (vividseats_data + seatgeak_data):
                ticket_data = TicketData(
                    timestamp=datetime.now(),
                    ticket_price=data["ticket_price"],
                    ticket_source=data["ticket_source"],
                    ticket_date=data["ticket_date"]
                )
                data_manager.update_data(ticket_data)

        # Perform analytics
        analytics_results = analytics.compile_analytics_report()

        # Save analytics data to a CSV file
        for analytics_data in analytics_results:
            data_manager.update_analytics_data(analytics_data)

        # Check if it's time to send an email report
        if datetime.now() - last_report_time >= timedelta(minutes=config.REPORT_FREQUENCY):
            emailer.send_email_report(analytics_results)
            last_report_time = datetime.now()

        time.sleep(config.SCRAPE_FREQUENCY * 60)

if __name__ == "__main__":
    main()
