 #------------------------set:sıralı değil, değiştirilemez, yinelenmez
fruits={"Starwberry","Pineapple","Watermelon","Grape","Watermelon","Apple"}
print(fruits)
print(len(fruits)) #tekrarlı eleman varsa sadece bir tane alır 

set_complex={"Sıla",18,True,"Ordu",52,False}
print(set_complex)
print(type(set_complex))  

my_set=set((1,7,8,5)) #bu şekilde de oluşturabiliriz  

#print(fruits[0]) şeklinde bir kullanım yapamayız çünkü set ögeleri indexli değil

for item in fruits:
    print(fruits)

#-------set metodları

#yeni bir öge eklemek için add() metodunu kullanabiliriz
fruits={"Starwberry","Pineapple","Watermelon","Grape","Watermelon","Apple"}
fruits.add("Fig")
print(fruits)

#update metodu ile başka setten veri çekme
fruits={"Starwberry","Pineapple","Watermelon"}
fruits2={"Grape","Watermelon","Apple"}
fruits.update(fruits2)
print(fruits)
#bir listi de bu metodla set'e ekleyebiliriz  
#update yerine ' |= ' bunu da kullanabiliriz  
fruits={"Starwberry","Pineapple","Watermelon"}
fruits2={"Grape","Melon","Apple"}
fruits3={"Cherry","Fig"}
fruits |= fruits2 | fruits3 
#update işlemi aslında matematikteki kümelerin birleşimi işlemini yapıyor

#remove,pop veya discard metodu ile veri kaldırma
fruits={"Starwberry","Pineapple","Watermelon","Grape","Watermelon","Apple"}
fruits.remove("Apple")
print(fruits)
#remove ile sette hiç olmayan bir veriyi kaldırmaya çalışırsak geriye hata döndürür. ama discard'da geriye hata dönmez
fruits.discard("Fig")
#pop rastgele bir ögeyi kaldırır. kaldırdığı ögeyi anlamak için onu bir veriableye atamamız gerekiyor
remove_item=fruits.pop()
print(remove_item)

#clear metodu ile set'in içini boşaltabiliriz
fruits={"Starwberry","Pineapple","Watermelon"} 
fruits.clear()
print(fruits)

#del anahtar sözcüğü ile set'i tamamen ortadan kaldırabiliriz  
del fruits
print(fruits)

#setleri birleştirme metodları

#union bizim orjinal setlerimize dokunmadan yeni bir set oluşturur
fruits1={"Starwberry","Pineapple","Watermelon"} 
fruits2={"Grape","Melon","Apple"}

result=fruits1.union(fruits2)
print(result)  

result=fruits1 | fruits2 
#union ile set ve tuple'ı birletirebiliriz  

#update metodunu da kullanabiliri, update orijinal stin yapısını değiştirir  

#intersection metodu ile iki setteki ortak ögeleri yazdırabiliriz. yani A kesişim B kümesinin elemanlarını yazdırır
setNumber1={1,3,2,4}
setNumber2={4,5,6,7}

result=setNumber1.intersection(setNumber2)
result=setNumber1 & setNumber2 #intersection metodu yerine kısaca bunu da kullanabiliriz 
print(result)

#intersection_update metodu ile orijinal metodu değiştirerek üstteki işlemin aynısını yapabiliriz
setNumber1={1,3,2,4}
setNumber2={4,5,6,7}

setNumber1.intersection_update(setNumber2)
setNumber1 &= (setNumber2) #kısa yolu  
print(setNumber1)

#difference-> matematikte A-B kğmesini bulmsk için kullsnılan metod. yani A da olup B de olamyan elemanları yazdırır
setNumber1={1,3,2,4}
setNumber2={4,5,6,7}
result=setNumber1.difference(setNumber2) #differenceyi farklı türler arasındada kullanabiliriz ama (-)'yı sadece set için kullanabiliyoruz
result=setNumber1-setNumber2 #kısa yol
print(result)

#difference_update metodu
setNumber1={1,3,2,4}
setNumber2={4,3,6,7}
setNumber1.difference_update(setNumber2) #difference direkt olarak orijinalini değiştirdiği için ayrı bir veriableye atmaya gerek yok
#setNumber1-=setNumber2 | setNumber3 kısa yolu budur
print(setNumber1) 

#symmetric_difference metodu-> A ile B kümesinin ortak elemanları dışındakş elemanlarını yazdırmak için kullanılır
setNumber1={1,3,2,4}
setNumber2={4,3,6,7}
result=setNumber1.symmetric_difference(setNumber2)
result=setNumber1 ^ setNumber2
print(result)

#symmetric_difference_update metodu
setNumber1={1,3,2,4}
setNumber2={4,3,6,7}
setNumber1.symmetric_difference(setNumber2)
setNumber1 ^= setNumber2 
print(setNumber1) 

#copy metodu  
fruits1={"Starwberry","Pineapple","Watermelon"} 
result=fruits1.copy()
print(result)

#isdisjoint-> bu metod iki setin ortak elemanı var mı yok mu onu döndürüyor varsa FALSE yoksa TRUE 
setNumber1={1,3,2,4}
setNumber2={4,3,6,7}
result=setNumber1.isdisjoint(setNumber2)
print(result)

#issubset->bir set başka bir setin içinde var mı onu kontrol eder.varsa TRUE yoksa FALSE
setNumber1={3,4}
setNumber2={4,3,6,7}
result=setNumber1.issubset(setNumber2)
result=setNumber1 <= setNumber2
print(result)

#issuperset-> bu sefer setNumber2 setNumber1'in içinde mi onu kontrol ediyoruz
setNumber1={1,2,3,4}
setNumber2={4,3,}
result=setNumber1.issuperset(setNumber2)
result=setNumber1 >= setNumber2
print(result)
