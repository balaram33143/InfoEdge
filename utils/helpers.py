from datetime import datetime

def format_datetime(dt):
    """
    Convert datetime object to a readable string format.
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def get_timestamp():
    """
    Return current timestamp as string.
    """
    return format_datetime(datetime.now())
