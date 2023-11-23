class Order():

    def __init__(self):
        self.order = []
        self.bill = 0
        self.menu = {'sandwich': 10, 'tea': 7, 'salad': 9, 'pizza': 20, 'coffee': 3, 'water': 1} 

    # add items from menu to order and total cost of items to bill
    def add_to_order(self, client_input):
        client_order = client_input

        if client_order in self.menu:
            price = self.menu[client_order]
            self.bill += price
            self.order.append(client_order)
        else:
            return f'We are fresh out of {client_order} today'



    # receipt, return order + total bill
    def receipt(self):
        return f"You have ordered: {', '.join(self.order)}, your final bill is {self.bill}£"