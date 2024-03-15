from flask import Flask
import requests
from datetime import datetime, timedelta
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

def fetch_csv(url):
    response = requests.get(url)
    # Assuming the CSV is simple and just contains emails; adapt parsing as needed
    emails = response.text.split('\n')[1:]  # Skipping header
    return emails

def send_email(recipients, subject, html_content):
    # Setup your SMTP server and credentials
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_password"
    from_email = smtp_user  # Email from

    # Setup email content
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ", ".join(recipients)

    part2 = MIMEText(html_content, 'html')
    msg.attach(part2)

    # Send email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(from_email, recipients, msg.as_string())
    server.quit()

@app.route('/')
def send_daily_email():
    # URL of the CSV on GitHub
    csv_url = 'https://raw.githubusercontent.com/yourusername/yourrepo/main/emails.csv'
    emails = fetch_csv(csv_url)
    
    # Assume a second CSV for content, fetch and parse as needed
    # For simplicity, I'm using static values
    subject = "Daily Update"
    html_content = "<html><body><h1>Hello!</h1><p>This is your daily update.</p></body></html>"
    
    send_email(emails, subject, html_content)
    
    next_run = datetime.now() + timedelta(days=1)
    return f"Emails sent! Next run is scheduled for {next_run}"

if __name__ == '__main__':
    app.run(debug=True)
