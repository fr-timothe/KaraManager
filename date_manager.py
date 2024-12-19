import datetime

def date_now():
    return datetime.datetime.now().strftime("%Y-%m-%d")
    
def hour_now():
    return datetime.datetime.now().strftime("%H:%M")

def hour_now_round():
    return datetime.datetime.now().strftime("%H:00")
    
def date_time_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def date_to_datetime(date_time):
    return datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")