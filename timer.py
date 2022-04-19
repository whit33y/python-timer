import time
import os
import math
import datetime

hours = int(input('How many hours:'))
minutes = int(input('How many minutes: '))
seconds = int(input('How many seconds: '))
hours = hours * 60 * 60
minutes = minutes * 60
seconds = seconds + hours + minutes
print(math.floor(seconds/3600))
print(seconds)
pozostalo = seconds

for a in range(1,pozostalo+1):
    os.system('clear')
    print(str(datetime.timedelta(seconds=pozostalo)))
    pozostalo-=1
    time.sleep(1)
print('KONIEC!')