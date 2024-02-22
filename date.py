from datetime import datetime
now=datetime.now()
print(now)
print(now.year)# текущий год
print(now.month)#текущий месяц
print(now.day)#текущий день
print(now.hour)#текущее время 


from datetime import datetime 
from datetime import timedelta 
dt= datetime.now()  # текущий момент времени 
print(dt.strftime("%Y-%m-%d %H:%M %S.%f"))