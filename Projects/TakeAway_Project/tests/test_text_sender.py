
from unittest.mock import Mock
from lib.text_sender import Sms
from lib.authentication import ACCOUNT_SID, AUTH_TOKEN, TO_NUMBER, FROM_NUMBER


def test_place_order():
    text_sender = Mock()
    text_sender.send_text.return_value = True
    

def test_send_text_():
    sms_mock = Mock()
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    from_number = FROM_NUMBER
    to_number = TO_NUMBER
    message = "Your order is on the way."
    sms_mock.send_sms(account_sid, auth_token, from_number, to_number, message)
    sms_mock.send_sms.assert_called_once_with(account_sid, auth_token, from_number, to_number, message)

# For privacy reasons auth_token and account_sid are saved in a private file
