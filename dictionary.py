#-------------------------dictionary:sıralı, değiştirilebilir, yinelenmez
#verileri anahtar:değer(key:value) şeklinde tutar  
#bir anahtara ait iki değer tutulamaz, en son hangş değer girilmişse o tutulur.bu list için gecerli değildir 
car={
    "brand":"Skoda",
    "model":"octavia",
    "year":1959
}
print(car)
print(car["brand"]) #anahtarı girip değere ulaşabiliriz 
print(len(car)) 

person=dict(name="Sıla",age=18,country="Türkiye")
print(person)

#verilere erişme
print(person["name"]) #veya get metodu kullanılabilir
print(person.get("name")) 

#keys metodu-> dictionary'deki tüm anaharların listesine ulaşmak istiyorsak kullanabiliriz
my_keys=car.keys()
print(my_keys)

#values metodu ile de değerlere ulaşabiliriz 
my_values=car.values
print(my_values)

#dict'e yeni veri eklemek
person=dict(name="Sıla",age=18,country="Türkiye")
person["student"]="Yes"
print(person)

#items metodu->item öge demek. items metodu anahtar değer çiftlerini bir list içerisindeki tuple'lar olarak yazdırır
car={
    "brand":"Skoda",
    "model":"octavia",
    "year":1959
} 
print(car.items())
#sonradan dict'te bir güncelleme yaptığımızda items metodunu yeniden çağırmamıza gerek yok, direkt olarak kendiliğinden güncellenir
#mesela
car["color"]="black"
print(car) #üstte yapılan değişiklik dicte hemen yansır

#update metodu ile verileri değiştirebiliyoruz
car.update({"year":2024})
print(car)
#veya direkt car["year"]=2024 şeklinde de değiştirebilirdik  

#dictionary'e veri ekleme. update'i burada da kullanabiliriz 
car["color"]="black"

#pop metodu->anahtar ismi girilen veriyi diler
car.pop("brand") #brand isimli anahtar ve onun değeri kaldırıldı

#popitem metodu-> son eklenen ögeyi kaldırır  
car.popitem()
print(car)

#del anahtar sözcüğü ile de istediğimizi veya direct olarak hepsini silebilriiz
#clear metodu ile de içini boşaltabiliriz

#döngülerde dic kullanımı
car={
    "brand":"Skoda",
    "model":"octavia",
    "year":1959
} 
for item in car:
    print(item) #anahtarları yazdırır sadece, değerlerini yazdırmaz
    print(car[item]) #değerleri almak istiyorsak

for item in car.values():
    print(item) #değerleri almak için farklı bir yöntem

for key_item,value_item in car.items:
    print(f"{key_item}-{value_item}") #anahatar değer çiftini birlikte yazdırmak için

#bir dict yalnızca yazarak kopyalanamaz
car2=car #bu işlem ile kopyalama yapmış olmayız. sonrasında car'da yaptığımız değişiklikler car2'de de görünür
car2=car.copy()
car2=dict(car) #başka bir kopyalama yöntemi

#bir idct içerisine farklı bir dict yazılabilir
myFriend={
    "friend1":{
        "name":"Zeynep",
        "age":18
    }
}
#döngü ile iç içe dict verilerine ulaşmak
for outer_key,outer_value in myFriend.items():
    print(outer_key)
    for inner_key in outer_value:
        print(inner_key)

#fromkeys metodu-> dict oluşturmaya yarar
myKeys=("key1","key2","key3")
myValue=7
result=dict.fromkeys(my_keys,myValue)
print(result)

#setdefault metodu-> bir dict'te bir anahtarın var olup olmadığını kontrol ediyor 
car={
    "brand":"Skoda",
    "model":"octavia",
    "year":1959
} 
result=car.setdefault("model","superb") #girilen anahtar mevcutsa onundeğerini getirir,yoksa öyle bir anahtar oluşturur ve girirlen değeri ona atar
print(result)
print(car)