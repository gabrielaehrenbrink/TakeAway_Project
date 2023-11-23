from lib.text_sender import Sms
from lib.delivery_estimation import DeliveryEstimation

class TakeAway:
    def __init__(self):
        self.menu = {'sandwich': 10, 'tea': 7, 'salad': 9, 'pizza': 20, 'coffee': 3, 'water': 1}
        self.bill = 0
        self.order = []

    def read_menu(self):
        formatted_menu = "Dishes:\t\t\t\t\t\t\tPrice:\n"

        max_dish_length = max(len(dish) for dish in self.menu.keys())

        for dish, price in self.menu.items():
            formatted_menu += f"{dish.ljust(max_dish_length)}\t\t\t\t\t\t{price}£\n"

        return formatted_menu

    def add_to_order(self, client_order):
        if client_order in self.menu:
            price = self.menu[client_order]
            self.bill += price
            self.order.append(client_order)
        else:
            return f'Sorry, we are fresh out of {client_order} today. Please try something else.'

    def receipt(self):
        return f"You have ordered: {', '.join(self.order)}, your final bill is {self.bill}£"

    def text_sender(self, account_sid, auth_token, from_number, client_number, message):
        to_numbers = [client_number]
        account_sid = 'ACa3f4836d8b69fee063ab09a13f95b0be'
        auth_token = '[AuthToken]'
        from_number = '+447893938522'
        message += f"\nEstimated delivery time: {DeliveryEstimation.get_one_hour_ahead_time()}"
        Sms.send_sms(account_sid, auth_token, from_number, to_numbers, message)
        return 'Text sent'