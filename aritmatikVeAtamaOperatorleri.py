#toplama çıkarma  çarpma mod alma C ile aynı 

x=5
y=2

#bölmek için tek slash(/) kullandığımızda bize sonucu float şeklinde virgülden sonrasıyla birlikte veriyor
print(x/y)
#çift slash(//) kullanırsak bölümün sadece tam kısmını verir
print(x//y)
#üs alma 
print(x**y)
#----bitsel düzeyde operatörler  
#x&y->bitsel düzeyde ve operatörüdür, x|y->bitsel düzeyde veya operatörüdür 

x=7
x &=12 #  buna bitsel düzeyde çarpma denir. 7 nin binary karşılığı ile 12 nin binary karşılığını çarpıyoruz
print(x) #=4

x=7
x |=12 #  buna bitsel düzeyde toplama denir. 7 nin binary karşılığı ile 12 nin binary karşılığını topluyoruz  
print(x) #=4

# ^ ->XOR işareti. true değeri için 1 0 veya 0 1 olmalı  

# >>= ->bitleri sağa doğru ötele demek. mesela x=16 olsun, x>>=3 demek bitleri iki birim sağa kaydırmak demek.Bu da x'i iki üzeri üçe bölmek anlamına geliyor. 
# <<= ->bitleri sola doğru ötele demek. mesela x=16 olsun, x<<=3 demek bitleri iki birim sola kaydırmak demek.Bu da x'i iki üzeri üç ile çarpmak anlamına geliyor  . 
#3<<2 =3*(2üzeri2)
#32>>2 =32/(2üzeri2)   
#:= -> atama operatörü kullanıldığı anda yeni bir atama yapıyor
x=7
print(x:=19)

# ~(not)-> sayıya bir ekler sonrada negatifine çevirir  
#-----karşılaştırma operatörleri
x=7 
y=9
print(x==y) #false

#!= eşit değil

#ÖRNEK
realPassword="12345"
myPassword=input("Enter the password:")

if realPassword==myPassword:
    print("that's true")
else:
    print("that's false")    

#ÖRNEK

number=int(input("Enter a number:"))

if number%2==0:
    print("that's number is even number")
else:
    print("that's number is odd number ")

#and-> C dilindeki &&, or->C dilindeki ||
x=7
print(x>5 and x<15) 
print(x>15 or x>5)
#birde not var, bu C de yok;  not(x>3 and x<15) şeklinde kullanılabilir  

#is ve is not nesnelerin aynı olup olmadığını komtrol eder
x=["starwberry","grape","pineapple"]
y=["starwberry","grape","pineapple"]
z=x
print(x is z)#z x'e eşitlendiği için bu true değeri alır  
print(y is z)#bu false gelir. y ile z nin içeriklerinin aynı olması bunların aynı nesne oldukları  anlamına gelmez
print(x==y)#içeriği karşılaştırmak istersek bunu kullanacağız  

#in ve not in  ->bir nesnenin bir seri içerisinde olup olmadığını kontrol etmek için kullanılır
fruits=["starwberry","grape","pineapple"]
print("grape"in fruits)
