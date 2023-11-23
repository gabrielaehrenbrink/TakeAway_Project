class Menu():
    def __init__(self):
        self._menu = {'sandwich': 10, 'tea': 7, 'salad': 9, 'pizza': 20, 'coffee': 3, 'water': 1}

    # add items to menu
    def add(self, food, value):
        self._menu[food] = value

    #  remove items from menu
    def remove(self, food):
        self._menu.pop(food)

    # read menu
    def read_menu(self):
        return self._menu