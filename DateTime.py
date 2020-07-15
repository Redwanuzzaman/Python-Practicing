import datetime

current_time = datetime.datetime.now()

print(current_time)  # 2020-07-16 03:33:43.226594
print(current_time.year)  # 2020
print(current_time.astimezone())  # 2020-07-16 03:35:14.805591+06:00
print(current_time + datetime.timedelta(days=365))  # 2021-07-16 03:36:20.656947 after 365 days time

