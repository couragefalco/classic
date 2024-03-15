from flask import Flask
import requests
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

app = Flask(__name__)

def fetch_csv(url):
    response = requests.get(url)
    data = response.text.split('\n')[1:]  # Skip header
    return [row.split(';') for row in data if row]  # Use semicolon as delimiter

def send_email(recipients, subject, html_content):
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')
    from_email = os.getenv('FROM_EMAIL')

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ", ".join(recipients)

    part2 = MIMEText(html_content, 'html')
    msg.attach(part2)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(from_email, recipients, msg.as_string())
    server.quit()

@app.route('/')
def send_daily_email():
    emails_csv_url = os.getenv('EMAILS_CSV_URL')
    content_csv_url = os.getenv('CONTENT_CSV_URL')

    emails = [email[0] for email in fetch_csv(emails_csv_url) if email]
    content_data = fetch_csv(content_csv_url)[0]  # Assuming single row for daily content

    if content_data and len(content_data) == 3:
        subject, picture_link, description = content_data
        description = description.replace('""', '"')

        # Load HTML content template from index.html
        with open('index.html', 'r', encoding='utf-8') as file:
            html_template = file.read()

        html_content = html_template.format(subject=subject, picture_link=picture_link, description=description)

        send_email(emails, subject, html_content)
        next_run = datetime.now() + timedelta(days=1)
        return f"Emails sent! Next run is scheduled for {next_run}"
    else:
        return "Failed to fetch content data or data is incomplete."

if __name__ == '__main__':
    app.run(debug=True)
