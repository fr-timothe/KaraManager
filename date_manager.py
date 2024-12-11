import datetime

def date_now():
    return datetime.datetime.now().strftime("%d-%m-%Y")
    
def hour_now():
    return datetime.datetime.now().strftime("%H:%M")
    
def date_time_now():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M")