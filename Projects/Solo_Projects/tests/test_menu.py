from lib.menu import Menu

def test_add_item_menu():
    menu = Menu()
    menu.add('burger', 10)
    result = menu.read_menu()
    assert result == {'sandwich': 10, 'tea': 7, 'salad': 9, 'pizza': 20, 'coffee': 3, 'water': 1, 'burger': 10}



def test_add_multiple_items_menu():
    menu = Menu()
    menu.add('burger', 10)
    menu.add('beer', 10)
    menu.add('wine', 7)
    result = menu.read_menu()
    assert result == {'sandwich': 10, 'tea': 7, 'salad': 9, 'pizza': 20, 'coffee': 3, 'water': 1, 'burger': 10, 'beer': 10, 'wine':7}


def test_remove_item_menu():
    menu = Menu()
    menu.add('burger', 10)
    menu.add('beer', 10)
    menu.add('wine', 7)
    menu.remove('tea')
    result = menu.read_menu()
    assert result == {'sandwich': 10, 'salad': 9, 'pizza': 20, 'coffee': 3, 'water': 1, 'burger': 10, 'beer': 10, 'wine':7}