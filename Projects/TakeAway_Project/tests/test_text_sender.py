
from unittest.mock import Mock
from lib.text_sender import Sms


def test_place_order():
    text_sender = Mock()
    text_sender.send_text.return_value = True
    

def test_send_text_():
    sms_mock = Mock()
    account_sid = 'ACa3f4836d8b69fee063ab09a13f95b0be'
    auth_token = '7d9a86a9a3b650272bb7562fbebb1f8c'
    from_number = '+447893938522'
    to_number = '+447307251340'
    message = "Your order is on the way."
    sms_mock.send_sms(account_sid, auth_token, from_number, to_number, message)
    sms_mock.send_sms.assert_called_once_with(account_sid, auth_token, from_number, to_number, message)
