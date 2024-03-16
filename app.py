from flask import Flask
import requests
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from string import Template

# Load environment variables
load_dotenv()

app = Flask(__name__)

def fetch_csv(url, delimiter=';'):
    response = requests.get(url)
    print(f"Fetching CSV from {url}, status code: {response.status_code}")
    data = response.text.split('\n')[1:]  # Skip header
    parsed_data = [row.split(delimiter) for row in data if row]
    print(f"Parsed CSV data: {parsed_data[:2]}")
    return parsed_data

def send_email(recipients, subject, html_content):
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')
    from_email = os.getenv('FROM_EMAIL')

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = ", ".join(recipients)
        part2 = MIMEText(html_content, 'html')
        msg.attach(part2)
        server.sendmail(from_email, recipients, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/')
def send_daily_email():
    emails_csv_url = os.getenv('EMAILS_CSV_URL')
    content_csv_url = os.getenv('CONTENT_CSV_URL')

    emails = [email[0] for email in fetch_csv(emails_csv_url, delimiter=',') if email]
    content = fetch_csv(content_csv_url)  # Fetch content data

    if content and len(content) > 0:
        content_data = content[0]  # Accessing the first row
        if len(content_data) == 3:
            subject, picture_link, description = content_data
            description = description.replace('""', '"')

            # Use Template for HTML content
            with open('index.html', 'r', encoding='utf-8') as file:
                src = Template(file.read())

            html_content = src.safe_substitute(subject=subject, picture_link=picture_link, description=description)

            send_email(emails, subject, html_content)
            next_run = datetime.now() + timedelta(days=1)
            return f"Emails sent! Next run is scheduled for {next_run}"
        else:
            return "Content data is incomplete."
    else:
        return "Failed to fetch content data or CSV file is empty."

if __name__ == '__main__':
    app.run(debug=True)
