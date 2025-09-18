## Small utility module for sending email https://docs.python.org/3/library/smtplib.html

import smtplib
from email.mime.text import MIMEText

def send_email(subject, msg_raw, recipient):
    # Gmail credentials
    sender = "your_gmail_address@gmail.com"
    password = "DON'T PUBLISH ACTUAL PASSWORDS ON THE INTERNET AS PLAINTEXT"
    # If you want your own: create one in https://myaccount.google.com/apppasswords
    # and please don't post it in the public internet 🙈

    # Create the email
    msg = MIMEText(str(msg_raw))
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    # Connect and send
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    print("Email sent successfully!")
