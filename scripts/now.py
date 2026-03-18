import datetime

WEEKDAYS = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

now = datetime.datetime.now()
print(f"{now.strftime('%Y-%m-%d %H:%M')} {WEEKDAYS[now.weekday()]}")
