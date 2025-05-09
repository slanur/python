import random

print(random.random())

#seed rastgele sayı uretecinden sabit bir sayı almak için kullanılır
random.seed(7)
print(random.random())
print("------------------------------------------")
#state ve getstate kullanımı
print(random.random()) #1. sayı

state=random.getstate()#bununla ikinci sayıyı kaydettik
print(random.random()) #2. sayı

print(random.random()) #3. sayı

random.setstate(state)#kaydedttiğimiz sayıyı geri çağırdık
print(random.random()) #2. sayı ile aynı olan bir 4. sayı geldi
print("---------------------------------------")

#getrandbits belirtilen bit boyutunda sayı dondurur
print(random.getrandbits(8)) 
print("------------------------------------------------")

#randrange verilen aralıkta rastgele bir sayı döndürür
print(random.randrange(1,10)) #1 dahil 10 dahil değil 
print(random.randrange(1,10,3)) #3. parametre artış miktarını verir 
print("-------------------------------------------------------")

#randint->verilen araıklalıkları ikiside dahil. rastgele tamsayılar döndürür  
print(random.randint(1,5)) 

#choice-->verilen seriden rastgele bir öge döndürür 
myList=["Apple","Grape","Banana","watermelon"] #illa list olamsına gerek yok string vs de olabilir 
print(random.choice(myList))

#choices 
myList=["Apple","Grape","Banana","watermelon"] 
print(random.choices(myList,weights=[10,1,1,1],k=19)) #weight hangisinden daha çok istediğimizi belirtir,üçüncü parametre ise toplamda kaç tane döndürmek istediğimizi belirtir 

#shuffle-> bir seriyi rastgele bir sırayla döndürür. orijinal sırayı değiştirir 
myList=["Apple","Grape","Banana","watermelon"] 
random.shuffle(myList)
print(myList)

#sample-> belirlenen listeden belirlenen sayı kadar rastgele öge getirir 
myList=["Apple","Grape","Banana","watermelon"] 
print(random.sample(myList,k=2))

#random-> sıfır ile bir arasında rastgele bir ondalıklı sayı döndürür
print(random.random())

#uniform-> verilen iki parametre arasında rastgele bir ondalıklı sayı döndürür 
print(random.uniform(30,70))

#triangular-> uniform ile aynı gibş ama girdiğimiz üçüncü parametre ile çoğunlukla  hangi sayıya yakın değerler döndürmesini istiyorsak onu girebillriz 
print(random.triangular(30,70,33))



