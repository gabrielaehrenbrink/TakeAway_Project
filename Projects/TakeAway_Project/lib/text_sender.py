
import os
from twilio.rest import Client
# from datetime import datetime, timedelta


class Sms():
    @staticmethod
    def send_sms(account_sid, auth_token, from_number, to_numbers, message):
        client = Client(account_sid, auth_token)

        for number in to_numbers:
            message = client.messages.create(
                body=message,
                from_=from_number,
                to=number
            )
            return f"SMS sent to {number} with SID: {message.sid}"
            
