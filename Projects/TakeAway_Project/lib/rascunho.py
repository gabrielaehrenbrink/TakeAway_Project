# import os
# from twilio.rest import Client
# from datetime import datetime, timedelta

# class Sms:
#     @staticmethod
#     def send_sms(account_sid, auth_token, from_number, to_numbers, message):
#         client = Client(account_sid, auth_token)

#         for number in to_numbers:
#             message = client.messages.create(
#                 body=message,
#                 from_=from_number,
#                 to=number
#             )
#             return f"SMS sent to {number} with SID: {message.sid}"

# class DeliveryEstimation:
#     @staticmethod
#     def get_one_hour_ahead_time():
#         current_time = datetime.now()
#         one_hour_ahead_time = current_time + timedelta(hours=1)
#         formatted_time = one_hour_ahead_time.strftime("%I:%M %p")
#         return formatted_time

# class TakeAway:
#     def __init__(self):
#         self.menu = {'sandwich': 10, 'tea': 7, 'salad': 9, 'pizza': 20, 'coffee': 3, 'water': 1}
#         self.bill = 0
#         self.order = []

#     def read_menu(self):
#         return self.menu

#     def add_to_order(self, client_order):
#         if client_order in self.menu:
#             price = self.menu[client_order]
#             self.bill += price
#             self.order.append(client_order)
#         else:
#             return f'Sorry, we are fresh out of {client_order} today. Please try something else.'

#     def receipt(self):
#         return f"You have ordered: {', '.join(self.order)}, your final bill is {self.bill}£"

#     def text_sender(self, account_sid, auth_token, from_number, client_number, message):
#         to_numbers = [client_number]
#         account_sid = 'ACa3f4836d8b69fee063ab09a13f95b0be'
#         auth_token = '7d9a86a9a3b650272bb7562fbebb1f8c'
#         from_number = '+447893938522'
#         message += f"\nEstimated delivery time: {DeliveryEstimation.get_one_hour_ahead_time()}"
#         Sms.send_sms(account_sid, auth_token, from_number, to_numbers, message)
#         return 'Text sent'