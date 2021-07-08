import smtplib
from twilio.rest import Client

TWILIO_SID = "ACc36296814fad27a4deaab9899530dcb6"
TWILIO_AUTH_TOKEN = "7d81f9ef1a2b2a28d833ea4f10774714"

TWILIO_VIRTUAL_NUMBER = "+14044713439"
TWILIO_VERIFIED_NUMBER = "+918320210032"

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "smeetautoreply@gmail.com"
MY_PASSWORD = "smeet1234!"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )