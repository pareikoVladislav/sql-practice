from datetime import datetime


def get_datetime_string():
    current_time = datetime.now()  # 2023-07-23 00:00:00.000000
    return datetime.strftime(current_time, "%y-%m-%d %H:%M:%S")
