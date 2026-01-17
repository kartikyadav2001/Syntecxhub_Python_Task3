import smtplib
import csv
import time
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_email(sender, app_password, subject, body, recipients_file, attachment=None):
    failed = []

    with open(recipients_file, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            email = row["email"]
            name = row.get("name", "User")

            msg = EmailMessage()
            msg["From"] = sender
            msg["To"] = email
            msg["Subject"] = subject
            msg.set_content(body.replace("{name}", name))

            if attachment:
                with open(attachment, "rb") as f:
                    msg.add_attachment(f.read(), filename=attachment)

            for attempt in range(3):
                try:
                    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
                        smtp.starttls()
                        smtp.login(sender, app_password)
                        smtp.send_message(msg)
                        print(f"Sent to {email}")
                        break
                except Exception as e:
                    print(f"Retry {attempt+1} failed for {email}: {e}")
                    time.sleep(2)

            else:
                failed.append(email)

    print("Failed to send:", failed)

if __name__ == "__main__":
    send_email(
        sender="your_email@gmail.com",
        app_password="your_app_password",
        subject="Test Email",
        body="Hello {name}, this is a test message!",
        recipients_file="recipients.csv",
        attachment=None
    )
