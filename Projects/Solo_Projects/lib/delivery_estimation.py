from datetime import datetime, timedelta

class DeliveryEstimation:
    @staticmethod
    def get_one_hour_ahead_time(current_time = datetime.now()): 
        one_hour_ahead_time = current_time + timedelta(hours=1)
        formatted_time = one_hour_ahead_time.strftime("%I:%M %p")
        return formatted_time
    
