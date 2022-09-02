from datetime import datetime
def make_datetime(t1, t2):
    t1_datetime = datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    t2_datetime = datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    return t1_datetime, t2_datetime

def time_delta(t1, t2):
    t1_datetime, t2_datetime = make_datetime(t1, t2)
    diff = int(abs(t1_datetime - t2_datetime).total_seconds())
    return str(diff)