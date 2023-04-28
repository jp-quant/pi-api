from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config
import smtplib


def format_report(analytics_data_list):
    report = "Analytics Report:\n\n"
    for data in analytics_data_list:
        report += f"Ticket Source: {data.ticket_source}\n"
        report += f"Ticket Date: {data.ticket_date}\n"
        report += f"Last Hour Lowest Price: {data.last_hour_lowest_price}\n"
        report += f"Last Day Lowest Price: {data.last_day_lowest_price}\n"
        report += f"Last Week Lowest Price: {data.last_week_lowest_price}\n\n"
    return report

from config import EMAIL_SENDER, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT, EMAIL_SUBJECT, EMAIL_RECIPIENTS

def send_email_report(analytics_data_list):
    report = format_report(analytics_data_list)
    
    # Set up email details
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = ', '.join(EMAIL_RECIPIENTS)
    msg['Subject'] = EMAIL_SUBJECT
    msg.attach(MIMEText(report, 'plain'))
    
    # Send email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

