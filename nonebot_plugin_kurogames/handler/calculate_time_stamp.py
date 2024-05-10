import time
from datetime import datetime, timedelta

def calculate_time_stamp(given_stamp, current_timestamp):

    # 计算两个时间戳之间的差值（以秒为单位）
    difference_seconds = given_stamp - current_timestamp

    # 将差值转换为天、小时和分钟
    days = difference_seconds // (24 * 3600)
    hours = (difference_seconds % (24 * 3600)) // 3600
    minutes = (difference_seconds % 3600) // 60

    # 输出结果
    return(f"{days}天{hours}小时{minutes}分")