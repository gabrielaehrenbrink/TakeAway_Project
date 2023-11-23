from lib.delivery_estimation import DeliveryEstimation
from datetime import datetime


def test_get_one_hour_ahead():
        delivery_estimation = DeliveryEstimation()
        one_hour_ahead_time ='10:24 AM'
        assert delivery_estimation.get_one_hour_ahead_time(datetime(2023, 11, 23, 9, 24)) == one_hour_ahead_time
        
  
