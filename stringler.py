print("hello")
print('hello')

#çoklu satır yazımı
text="""
this is so good
life is so good 
multiline strings
"""
#3 tane tek tırnak da kullanılabilir 
print(text)

#stringlerde bir dizidir. ayrıca python dizi için listleri kullanıyor 

cars=["BMW","Volvo","Skoda","Nissan"]
print(cars[0])

text="Python is good"

#stringin uzunluğunu len fonksiyonuyla alabiliriz 
print(len(text))

#in-> belirli bir ifadenin veya karakterin string içinde bulunup bulunmadığını kontrol etmek için kullanılır  

text="The best languages are free in life"
print("best" in text) #varsa true, yoksa false döndurecek

#not in ise içinde bulunmuyorsa true döndürür  

#slicing strings(stringlerde dilimleme )
text="python is weird"
print(text[1:5]) 
#1 den 5 e kadar olan ifadeleri yazdırır. 1 dahil 5 dahil değil  
#dilimlemeyi tersten yapmak için sayıları negatif yapmak gerekir 

#string concatenation(string birleştirme)
text="python"
text2="is weird" 
result=text +" "+ text2
print(result) 

#modify strings(stringleri  değiştirme)
text=" python is DOING well "
print(text.upper()) #tüm harfleri buyuk harfe cevirir

print(text.lower()) #tüm harfleri kucuk harfe cevirir

print(text.strip()) #girilen ifadenin başında veya sonunda  yanlışlıkla bırakılan boşlukları siler

print(text.replace("P","T")) #bu şekilde P harfini R harfi ile değiştirebiliriz 

text2="python, Java, C#"
print(text.split(",")) #verilenleri virgülden virgüle ayırır ve liste şeklinde getirir(burada virgülden farklı bir şey de olabilir)

#"Python" un octal sayı sisteminde yazımı
print("\120\171\164\150\157\156") 

#"Python" un hexadesimal sayı sisteminde yazımı
print("\x50\x79\x74\x68\x6F\x6E")

#string formatlama 
age=18
name="Silanur Candir"
text=f"My name is {name}, I am {age}" #f-string 
print(text)
price=19.4751
text=f"The price is {price:.2f} turkish money"
print(text)

#capitalize-> ilk harfi buyuk harf yapar
text3="welcome to my world. how is it going?"
print(text3.capitalize())

#casefold-> stringin tamamını kucuk harfe dönüştürür. görev olarak lower ile aynıdır ama lower'a göre daha güçlüdür
text3="welcome to my world. how is it going?"
print(text3.casefold())

#title->her kelimenin ilk harfini büyük harfe dönüştürür
text3="welcome to my world. how is it going?"
print(text3.title())

#swapcase->kücük harfi buyuğe, buyuk harfi kucuge cevirir
text3="Welcome to my world. How is it going?"
print(text3.swapcase())

#islower-> bir stringdeki tüm karakterler kucuk harfse true değeri döner
text3="welcome to my world. how is it going?"
print(text3.islower ())
#isupper'da tam tersi. tum harfler buyukse true değeri donuyor

 #center-> stringi ortalar. mesela 20 birimlik bir stringin tam ortasına koyar 
text="Hello python"
print(text.center(20))
print(text.center(20,"*")) #ikinci bir parametre daha alır ve bıraktığı boşlukları bununla doldurur  

#character encoding(karakter kodlama) ASCII karakterlere göre kodlama yapılması
print(ord("F"))
print(bin(70))
print((127).bit_length())
#ASCII karakter tablosu 7 bite uygun olarak yapılmıştır 
#unicode->universal code(evrensel code):ASCII nin eksikliklerini gidermek için ortaya çıktı  

#count->bir cümlede istenilen kelimeden kaç tane olduğunu verir 
text="Welcome to my world. My world is python"
print(text.count("world"))
#ikinci ve üçüncü parametreleride girerek hangi indexten aramaya başlayacağını ve nerede biteceğini belirtebiliriz  

#startswith->string istenilen değerle başlıyorda true döndürür
text="Welcome to my world. My world is python"
print(text.startswith("Welcome"))
print(text.startswith("Wel"))
#buradada başlangıc ve bitiş parametresi girebiliriz.girdiğimiz parametre istediğimiz karakter ile başlıyorsa true döner  

#endswith->string istenilen değerle bitiyorsa true döndürür 
text="Welcome to my world. My world is python"
print(text.endswith("python "))
#buradada başlangıc ve bitiş parametresi girebiliriz.girdiğimiz parametre istediğimiz karakter ile bitiyorsa   true döner  

#expandtabs->boşlukları ayarlamak için
text="p\ty\tt\th\to\tn"
print(text.expandtabs()) #hiçbirşey girmediğimizde 8 olarak kabul eder
print(text.expandtabs(2))

#find->cümle içinde istediğimiz stringin index nuumarasını döndürür.Eğer yoksa -1 döndürür 
text="Welcome to my world. My world is python"
print(text.find("to")) 
print(text.find("o")) 
print(text.find("a"))
#buradada başlangıç ve bitiş parametresi girebiliyoruz 

#index->find ile aynı görevde.Stringin index numarasını döndürüyor. Find ile farkı; eğer index numarası bulamazsa hata mesajı verir
text="Welcome to my world. My world is python"
print(text.index("python"))

#isalnum-> 0-9, a-z, A-Z dışındaki tüm karakterlere false verir 
text="Python3"
print(text.isalnum())  

#isalpha->a-z, A-Z sadece harfler için true döndürür 
text="Python"
print(text.isalnum())  

#isascii->ASCII karakter kodunda varsa true 
text="Python"
print(text.isascii())
text="çok" 
print(text.isascii())

#isdecimal->sadece sayıya true döndürür
text="123 "
print(text.isdecimal())

#isinstance->bir değişkenin belirli bir veri tipinde olup olmadığını kontrol etmek için kullanılır.eğer doğru tipteyse true döner 
x=70
print(isinstance(x,int)) 

#format string metodu
text1="my name is {fname}, I'm {age} years old".format(fname="Sıla",age=18)
text2="my name is {0}, I'm {1} years old".format("Sıla",18)
text3="my name is {}, I'm {} years old".format("Sıla",18)
print(text1)
print(text2)
print(text3)

#--------------------formatlama türleri
text="We dont have {:<10} children" #burada format içindeki 7 yi yazdıktan sonra(sola hizlı bir şekilde yazacak) 10 tane boşluk bırakacak
print(text.format(7))
#:> bu şekilde yazarsak sağa hizalı bir şekilde yazar 

#mevcut alan içinde stringi ortaya yazdırmak için
text="We dont have {:^10} children" 
print(text.format(7))

#bir sayıyı binary sisteme çevirmek istiyorsak
text="the binary versiyon of {0} is {0:b}"
print(text.format(6))

#string metodlar devamm

#isdigit->hepsi rakamsa true
text="709821"
print(text.isdigit())

#isidentifier(tanımlayıcı  )-> a-z,0-9 ve _ içerebilir. sayı ile başalayamaz 
a="SılaÇandır"
b="Sıla_Çandır"
c="Sıla Çandır"
d="1Sıla Çandır"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

#isnumeric->hepsi rakamsa true
text="70821"
print(text.isnumeric())

#isprintable->stringdeki tüm karakterler yazdırılabiliyorsa true. kaçış karakterleri azdırılamadığı içn varsa false döndürür
text="Sıla\nÇandır"
print(text.isprintable()) 

#isspace->stringin hepsi boşluktan oluşuyorsa true döndürür  
text="Sıla Çandır"
print(text.isspace()) 

#istitle->her kelimenin ilk harfi büyükse true değeri döndürür
text="Welcome To My World. My World Is Python"
print(text.istitle()) 

#join->stringleri birleştirmek için kullanılır
Names=("Sıla","Zeynep","Şeyma","Ebrar")
result=",".join(Names) #virgül yerine başka bir şey de kullanabiliriz  
print(result)

Names=("Sıla","Zeynep","Şeyma","Ebrar")
mySeperator=","
result=mySeperator.join(Names)
print(result) #aynı şeyi bu şekildede yazdırabiliriz 

#join'in dict ile kullanımı
myInfo={"Name":"Sila","country":"Türkiye"}
mySeperator=","
result=mySeperator.join(myInfo) 
print(result)
result=mySeperator.join(myInfo["Name"]) #dict içindeki bir değeri  yazdırmak istersek böyle kullanıyoruz
print(result)

#ljust->stringi sola yatırır
text="strawberry"
result=text.ljust(20) #strawberry 10 karakter. geri kalan 10 da boşluk için ayrıldı.ikincş bir parametre girerek boşluk yerine başka bir şey yazdırabiliriz
print(result,"is my favorite fruit") 
#rjust ise tam tersi. stringi sağa yaslar  

#örnek:vize ve finalin ortalaması
midterm_exam_score=input("Enter the midterm exam score:")
final_exam_score=input("Enter the final exam score  :")
#input ile kullanıcıdan string türünde veri alırız. bu yüzden bunu int'e veya floata çevirmeliyiz
avarage_score =(int(midterm_exam_score)+int(final_exam_score))/2
print(f"result is {avarage_score}")