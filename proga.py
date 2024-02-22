god=input('Укажите ваш год рождения')
god=int(input)
from datetime import datetime
now=datetime.now()
norma=now-god
while norma<=2 or norma>=200:
 print('возраст не подходит')





