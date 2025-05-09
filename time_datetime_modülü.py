from datetime import datetime #bu datetime modülünden sadece datet ime sınıfını dahil et demek  
 
#dir hazır metodu ile datetime modülü içindekileri görebiliriz
result=dir(datetime)
print(result)

result=datetime.datetime.now() #şuanın tarihini almak için kullanılır
print(result)

#kendi tarihimizi yazdırmak için
result=datetime(2007,1,13) #istersek saat parametrelerini de girebiliriz  
print(result)

#şuanın sadece gününü, ayını vs alabilriz
now_date=datetime.now()
print(now_date.day)
print(now_date.month)
print(now_date.year)
print(now_date.hour)
print(now_date.minute)
print(now_date.second)
print(now_date.microsecond)

print(type(now_date)) #integer veri türüdür  

now_date=datetime.today() #şuanı bu şekilde de alabiliriz 
now_day=datetime.weekday()#haftanın kaçıncı günü olduğunu yazdırır

now_date=datetime.ctime() #şuanı daha ayrıntılı bir şekilde alabiliriz 

from datetime import timedelta
#iki tarih farkı
date1=datetime(2025,1,15)
date2=datetime(2025,1,8)

difference=date1-date2
print(difference)

#döngülerle timedelta kullanımı
start_date=datetime(2025,1,1)
for item in range(14):
    print(start_date+timedelta(days=item))

#time sınıfı kullanımı
from datetime import time
my_time=time(14,20,34)
print(my_time)
print(my_time.hour)
print(my_time.minute)
print(my_time.second)

#time modülü
import time
from datetime import datetime
today=datetime.now()
print(today)

time.sleep(7) #kodu 7 saniye bekletiyor ve sonraki kodu öyle çalıştırıyor

today=datetime.now()
print(today) 