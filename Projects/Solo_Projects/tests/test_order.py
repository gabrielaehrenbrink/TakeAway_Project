from lib.order import Order


def test_add_one_item_to_order():
    order = Order()
    order.add_to_order('tea')
    assert order.receipt() == "You have ordered: tea, your final bill is 7£"


def test_add_multiple_items_to_order():
    order = Order()
    order.add_to_order('tea')
    order.add_to_order('salad')
    order.add_to_order('pizza')
    assert order.receipt() == "You have ordered: tea, salad, pizza, your final bill is 36£"

def test_add_repeated_items_to_order():
    order = Order()
    order.add_to_order('tea')
    order.add_to_order('tea')
    order.add_to_order('pizza')
    assert order.receipt() == "You have ordered: tea, tea, pizza, your final bill is 34£"


def test_unavailable_item_to_order():
    order = Order()
    result = order.add_to_order('banana')
    assert result == 'We are fresh out of banana today'