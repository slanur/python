#------------------------tuple: sıralı(yani indexlidir), değiştirilemez, yinelenebilir
fruits=("Starwberry","Pineapple","Watermelon","Grape","Watermelon","Grape") 
print(fruits)
print(len(fruits)) #öge sayısını bulmak için  

fruit=("strawberry",) #tek ögeli bir tuple oluşturmak için sonuna virgül bırakmalıyız.
fruit=("strawberry") #bu şekilde bir tuple değil string oldu
complex_tuple=("Sıla",18,"Ordu",True) #bu şekilde farklı veri türlerini tek bir tuple içinde tutabiliyoruz
fruit=tuple(("Starwberry","Pineapple","Watermelon","Grape","Watermelon","Grape"))

#tuple ögelerine erişim
fruits=("Starwberry","Pineapple","Watermelon","Grape","Watermelon","Grape") 
print(fruits[1])
print(fruits[2:5]) #2 den başlayıp 5. ye kadar yazdırır. 5 dahil değil

#bir öge tuple içerisinde var mı
fruits=("Starwberry","Pineapple","Watermelon","Grape","Watermelon","Apple")
search="Apple"
if(search in fruits):
    print(f"yes,{search} is in the fruits tuple")
else:
    print(f"no,{search} is not in the fruits tuple")

#iki adet tuple'ı birleştirmek için '+' operatörü kullanabiliriz
fruits=("Starwberry","Pineapple","Watermelon","Grape")
numbers=(1,2,3,4)
join_tuple=fruits+numbers
print(join_tuple)

#tuple ögelerini çarpım ile çoğaltma. bu şekilde çarptığımız sayı kadar tuple ögeleri tekrar eder
fruits=("Starwberry","Pineapple","Watermelon","Grape")
multiply_fruits=fruits*2
print(multiply_fruits)

#tuple güncelleme. normalde tuple ögeleri değiştirilemez, eklenemez,çıkarılamaz ama tuple'ı bir liste dönüştürürp oradan değişiklikler yapabiliriz 
fruits=("Starwberry","Pineapple","Watermelon","Grape","Watermelon","Apple")
temp_fruits=list(fruits)
temp_fruits[2]="kiwi"
fruits=tuple(temp_fruits)
print(fruits)

#tuple veri eklemek için ilk önce onu liste dönüştürüyoruz, verimizi ekleyip sonradan tekrar tuple'a dönüştürüyoruz
fruits=("Starwberry","Pineapple","Watermelon","Grape","Watermelon","Apple")
temp_fruits=list(fruits)
temp_fruits.append("kiwi")
fruits=tuple(temp_fruits)
print(fruits)

#bir tuple'a tuple ekleyebiliyoruz. bu yolu kullanarak da veri ekleyebiliriz  
fruits=("Starwberry","Pineapple","Watermelon","Grape","Watermelon","Apple")
extra_fruits=("kiwi",)
fruits+=extra_fruits
print(fruits)

#tuple'ı liste dönüştürerek veri silebiliriz
fruits=("Starwberry","Pineapple","Watermelon","Grape","Watermelon","Apple")
temp_fruits=list(fruits)
temp_fruits.remove("apple")
fruits=tuple(temp_fruits)
print(fruits)

#oluşturduğumuz tuple'ı tamamen ortadan kaldırmak için del anahtar sözcüğğünü kullanabiliriz
fruits=("Starwberry","Pineapple","Watermelon","Grape","Watermelon","Apple")
del fruits
print(fruits)

#paketleme ve paketten çıkarma(packing and unpacking) 
fruits=("Starwberry","Pineapple","Watermelon") #bu şekilde tuple içine değerler girmemiz packing işlemidir
(x,y,z)=fruits
print(x)
print(y)
print(z)#bunlarda paketten çıkarma işlemleridir(unpacking)
#eğer veriable'dan fazla öge varsa son veriable'ın başına '*' işareti bırakıyoruz. bu kalan ögeleri liste şeklinde tutmamızı sağlıyor

#tuple ile for döngüsü kullanımı
fruits=("Starwberry","Pineapple","Watermelon","Grape","Watermelon","Apple")
for item in fruit:
    print(item)
    
for item in range(len(fruits)):
    print(fruits[item])

#tuple ile while döngüsü
fruits=("Starwberry","Pineapple","Watermelon","Grape","Watermelon","Apple")
i=0
while(i<len(fruits)):
    print(fruits[i])
    i+=1

#count ve index metodları
#count ile bir ögenin bir tuple'da kaç tane olduğunun saısını alabiliriz,index ile de index numarasını alabiliriz
fruits=("Starwberry","Pineapple","Watermelon","Starwberry","Pineapple","Starwberry","Pineapple")
print(fruits.count("Strawberry"))
print(fruits.index("Pineapple")) #bir ögeden birden fazla varsa ilk bulduğu yerin indexini dönderir  