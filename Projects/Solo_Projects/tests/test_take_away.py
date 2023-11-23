from lib.take_away import TakeAway

def test_read_takeaway_menu():
    take_away = TakeAway()
    result = take_away.read_menu()
    assert result == 'Dishes:\t\t\t\t\t\t\tPrice:\nsandwich\t\t\t\t\t\t10£\ntea     \t\t\t\t\t\t7£\nsalad   \t\t\t\t\t\t9£\npizza   \t\t\t\t\t\t20£\ncoffee  \t\t\t\t\t\t3£\nwater   \t\t\t\t\t\t1£\n'

def test_add_unavailable_item_to_order():
    take_away = TakeAway()
    take_away.add_to_order('tea')
    assert take_away.receipt() == "You have ordered: tea, your final bill is 7£"

def test_add_multiple_items_to_order():
    take_away = TakeAway()
    take_away.add_to_order('tea')
    take_away.add_to_order('salad')
    take_away.add_to_order('pizza')
    assert take_away.receipt() == "You have ordered: tea, salad, pizza, your final bill is 36£"

def test_add_repeated_items_to_order():
    take_away = TakeAway()
    take_away.add_to_order('tea')
    take_away.add_to_order('tea')
    take_away.add_to_order('pizza')
    assert take_away.receipt() == "You have ordered: tea, tea, pizza, your final bill is 34£"


def test_unavailable_item_to_order():
    take_away = TakeAway()
    result = take_away.add_to_order('banana')
    assert result == 'Sorry, we are fresh out of banana today. Please try something else.'

def test_text_sender():
    take_away = TakeAway()
    to_numbers = '+447307251340'
    account_sid = 'ACa3f4836d8b69fee063ab09a13f95b0be'
    auth_token = '[AuthToken]'  
    from_number = '+447893938522'
    message = 'example message'
    take_away.text_sender(account_sid, auth_token, from_number, to_numbers, message)
    result = 'Text sent'
    assert result == 'Text sent'