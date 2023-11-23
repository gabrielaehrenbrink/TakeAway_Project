
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
            
        
    # def __init__(self, account_sid, auth_token, from_number):
    #     self.account_sid = account_sid
    #     self.auth_token = auth_token
    #     self.from_number = from_number

    # def send_sms(account_sid, auth_token, from_number, to_number, message):
    #     client = Client(account_sid, auth_token)

    #     try:
    #         message = client.messages.create(
    #             body=message,
    #             from_=from_number,
    #             to=to_number
    #         )
    #         print(f"SMS sent with SID: {message.sid}")
    #     except Exception as e:
    #         print(f"Failed to send SMS: {e}")

    # def get_one_hour_ahead_time():
    #     current_time = datetime.now()
    #     one_hour_ahead_time = current_time + timedelta(hours=1)
    #     formatted_time = one_hour_ahead_time.strftime("%I:%M %p")
    #     return formatted_time

    # #Twilio account SID and Auth Token
    # account_sid = 'ACa3f4836d8b69fee063ab09a13f95b0be'
    # auth_token = '7d9a86a9a3b650272bb7562fbebb1f8c'

    # #Twilio number and the number you want to send the SMS to
    # from_number = '+447893938522'
    # to_number = ''

    # #SMS message
    # message = f"Thank you! Your order was placed and will be delivered before {get_one_hour_ahead_time()}."

    # send_sms(account_sid, auth_token, from_number, to_number, message)