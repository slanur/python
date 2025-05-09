#array= list, tuple, set, dictionary

#-----------------------list: sıralı, değiştirilebilir, tekrarlayabilir
fruits=["starwberry","grape","pineapple"]
#indexNum=[0],        [1]        [2]      veya
#         [0]         [-2]         [-1]
print(fruits)
print(fruits[0:3])#bu sıfırıncı indexten başla ve 3. index'e kadar yazdır demek . 3 dahil değil

if "grape" in fruits:
    print("there is grape in fruits") #bir elemanın bir seri içerisinde olup olamdığı bu şekilde kontrol edilebilir

fruits[1]="watermelon" #list elemanı bu şekilde sonradan değiştirilebilir  veya
fruits[0:3]="cherry" 
#eğer değiştirirken liste daha fazla eleman eklemeye çalışırsak, o fa<ladan eklediğimiz elemana da yer açıyor  

fruits=["starwberry","grape","pineapple"]+["watermelon","starwberry","grape","pineapple"] #list'e bu şekilde eleman ekleyebiliriz 


myList=["Sıla",18,"Ordu",52]
print(myList)
print(type(myList))#list adında bir veri türü gelir  

myList=((1,2,3,4)) #list'i bu şekilde iki tane parantez kullanarak da oluşturabiliriz  

#bir listin kaç elemandan oluştuğunu bulmak için len fonksiyonu kullanılabilir 

# aşağıda tekrarlı bir listi tekrarsız hale getirip yazma işlemi yapıldı 
fruits=["starwberry","grape","pineapple","orange","pineapple","melon","watermelon","starwberry","grape","pineapple"]  
fruits=list(dict.fromkeys(fruits))
print(fruits)

#-----list'e eleman eklemek için bazı metodların kullanılması önerilir
#eğer list'in sonuna bir eleman eklemek istiyorsak append() kullanabiliriz
fruits=["starwberry","grape","pineapple"]
fruits.append("cherry")
print(fruits)

#eğer belirli bir elemanın yerine başka bir eleman eklemek istiyorsak  insert() kullanabiliriz
fruits.insert(1,"apple") #şimdi 1. indexe apple geldi ve grape bir index kayarak 2 oldu

#eğer liste başka bir list eklemek istiyorsak extend() kullanabiliriz. sadece list için değil diğer array türlerini de bu şekilde ekleyebiliriz  
fruit1=["starwberry","grape","pineapple"]
fruit2=["pineapple","melon","watermelon"]
fruit1.extend(fruit2)
print(fruit1)

#--------list kopyalama 
 #listler diğer veriableler gibi new_fruit=fruit1 şeklinde kopyalanamaz.Bu şekilde yapılırsa kopya değil birbirinin aynısı iki
#list oluşur ve birindeki değişiklik diğerini de etkiler. bu yüzden kopya oluşturmak için copy() metodunu kullanabilriz 
new_fruit=fruit1.copy()
print(new_fruit)
#ikinci olarak list() metodunu kullanabilriz
new_fruit2=list(fruit1)
print(new_fruit2)
#üçüncü olarak slice [:] operatörü ile kopya oluşturabiliriz
new_fruit3=fruit1[:]
print(new_fruit3) 

#eğer list içinde list verilmişse bunu copy() kütüphanesi ile kopyalayabiliriz  
import copy
list1=[[1,2],[3,4]]
new_list=copy.deepcopy(list1)

#ögeleri list'ten kaldırmak için remove kullanabiliriz
fruits=["starwberry","grape","pineapple"]
fruits.remove("grape")
print(fruits)

#pop metodu son ögeyi kaldırmak için kullanılır
fruits=["starwberry","grape","pineapple"]
fruits.pop() #pop bize serinin son elemanını döndürür. İstersek bunu başka bir değişkene de atayabiliriz 
print(fruits)
#pop'a index numarası girerek istediğimiz ögeyi de sildirebiliriz

#del ile de istediğimiz ögeyi kaldırabiliriz. del'de if gibi pythondaki bir anahtar sözcüktür 
fruits=["starwberry","grape","pineapple"]
del fruits[1]
#del fruits yaparak fruits adındaki listeyi direkt yok edebilriz

#clear metodu ile listenin içini boşaltabiliriz
fruits=["starwberry","grape","pineapple"]
fruits.clear()
print(fruits)
 
#index metodu ile istediğimiz ögenin index numarasını öğrenebilriz 
#count metodu da bir ögenin list'te kaç tane bulunduğunu bize verir  


#---------------listeleri sıralama(sort list)
#sayıları küçükten büyüğe ve stringleri a'da z'ye sıralayabilmek için sort metodu kullanılır

myFruits=["Starwberry","Pineapple","Watermelon","Grape"] #büyük,küçük harf duyarlılığına dikkat etmemiz gerekiyor
#yoksa büyük harflileri kendi arasında, küçük harflileri kendi arasında sıralar 
myNumbers=[19,7,32,52,27]
myFruits.sort()
myNumbers.sort()
print(myFruits)
print(myNumbers)
#eğer büyük,küçük harf duyarlılığını ortadan kaldırmak istiyorsak
myFruits.sort(key=str.lower) #tüm harfleri küçük olarak algılayıp ona göre sıralama yapacak  

#eğer büyükten küçüğe veya z'den a'ya sıralanmasını istiyorsak reverse kullanacağız
myFruits.sort(reverse=True)
myNumbers.sort(reverse=True) 

#eğer listleri tersten yazdırmak istersek reverse kullanmalıyız
myNumbers.reverse()
myFruits.reverse()
print(myFruits)
print(myNumbers)  
