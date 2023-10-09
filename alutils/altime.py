from datetime import datetime
from pytz import timezone

def get_timestamp():
    fmt = "%Y%m%d_%H%M%S"

    now_utc = datetime.now(timezone('Hongkong'))
    time_index = now_utc.strftime(fmt)[2:]

    return time_index