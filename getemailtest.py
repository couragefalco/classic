import imaplib
import os
import email

# Email account credentials and server details
EMAIL_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_ACCOUNT = "classic@havecourage.de"
IMAP_SERVER = "imap.strato.de"
IMAP_PORT = 993

# Connect to the IMAP email server
def connect_to_email_server():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        return mail
    except imaplib.IMAP4.error as error:
        print(f"Error connecting to the email server: {error}")
        return None

def fetch_and_print_emails(mail):
    mail.select('inbox')
    typ, data = mail.search(None, 'ALL')
    if typ != 'OK':
        print("No messages found!")
        return

    email_ids = data[0].split()
    print(f"Total emails: {len(email_ids)}")
    email_ids.reverse()

    for num in email_ids:
        typ, data = mail.fetch(num, '(RFC822)')
        if typ != 'OK':
            print(f"Error fetching mail {num.decode()}")
            continue

        msg = email.message_from_bytes(data[0][1])
        subject = msg['subject']
        print(f"Email {num.decode()}: {subject}")

# Main function
def main():
    mail = connect_to_email_server()
    if mail:
        fetch_and_print_emails(mail)
        mail.close()
        mail.logout()

if __name__ == '__main__':
    main()
