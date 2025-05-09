#fonksiyon oluşturma
def my_function():
    print("now")
    print("i can write a function")

my_function()

#argüman ve parametre kullanımı
def my_name(fname):
    print(fname+ "Çandır")

my_name("Sıla")

def fullName(firstName,lastName):
    print(firstName+" "+lastName)

fullName("Sıla","Çandır") #parametre kadar argüman göndermek gereiyor yoksa hata çıkar 

#fonksiyona kaç adet argüman göndereceğimiz belli değilse * işareti bırakmak gerekiyor
def my_Name(*name):
    print("my real name is "+name[2])

my_Name("sıla","zeynep","esma")

#bir fonksiyonu bir veriable'a atıp sonradan veriable'ı fonksiyon gibi çağırabiliriz
def greeting():
    print("hello")
g=greeting
g()  

#argümanları anahtar değer çifti olarak gönderme
def Name(name3,name2,name1):
    print("my name is "+name3)
Name(name1="esma",name2="zeynep",name3="sıla")

#belirsiz sayıda argüman varsa
def My_Name(**unKnown):
    print("his last name is "+unKnown["lastname"])

My_Name(firstname="Sıla",lastname="Çandır")

#fonksiyona eğer argüman girilmemişse fonksiyon varsayılan(default) argümanı kullanır
def my_country(country="Türkiye"):
    print("I am from "+country)

my_country("Norway") #eğer bir argüman girilmişse onu yazar girilmemişse Türkiye yazar
my_country()

#bir function'a herhangi bir veri türünde argüman girebiliriz

#bir function'un geriye  bir değer döndürmesini istiyorsak return anahtar sözcüğünü kullanmamaız gerekiyor
def my_math_function(x):
    return x*7
print(my_math_function(3))  

#döngü içnde fonksiyon kullanma 
def Hello():
    print("hello")

for item in range(7):
    Hello()

#bir fonksiyonu başka bir fonksiyon içinde çalıştırmak
def square(number):
    return number**2

def sum_and_square(x,y):
    sum_result=x+y
    return square(sum_result)

result=sum_and_square(3,4)
print(result)

#iç içe fonksiyon kullanımı  
def outer_function(name):
    def greeting():
        return f"Hello, {name}!"
    return greeting()

print(outer_function("Sıla"))

#return komutuyla birden fazla değer gönderme 
def sum(x,y):
    return x+y
def multiply(x,y):
    return x*y
def calculation(x,y):
    sum_result=sum()

#bir fomksiyonu başka bir fonksiyona parametre olarak gönderme
def multiply(number):
    return number*7
def myFuncion(func_name,my_value):
    return func_name(my_value)
result=myFuncion(multiply,10)
print(result)

#yerel olarak kullanılan bir x değişkeni global x komutuyla global olarak kulanılabilir
#nonlocal komutu->iç içe geçmiş fonksşyonlarda içteki fonksiyonun dıştaki bir değişkenin değerini değiştirmesine yardımcı olur

# recursion fonksiyon ile faktöriyel hesaplama
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print(fact(6))

# recursion fonksiyon ile fibonacci serisi
def fib(n):
    if(n<=0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)

for item in range(6):
    print(fib(item),end=" ") 

# recursion fonksiyon ile toplama işlemi
def sum_recursion(n):
    if(n>0):
        result=n+sum_recursion(n-1)
    else:
        result=0
        return result
print(sum_recursion(6))
#recursion toplamaya en sondan başlar 

