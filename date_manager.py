import datetime

def date_now():
    return datetime.datetime.now().strftime("%Y-%m-%d")
    
def hour_now():
    return datetime.datetime.now().strftime("%H:%M")
    
def date_time_now(self):
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")