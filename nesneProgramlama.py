#belli fonksiyonların bir kümede birleştirilmesine class denir  

#nesne programlamada class'ların içindeki veriable yerine->property(özellik) fonsiyon yerine-> metod isimlerini kullanacağız

#class oluşturma ve kullanma
class myClass:
    """
    Burayı class'ı açıklamak için kullanıyoruz
    """
    x=7

obj=myClass()
print(obj.x)

class vehicle: #(araç)
    brand="skoda"
    model="superb"
    color="white"
#aşağıdaki satır ile nesne oluşturmuş oluyoruz
car_obj=vehicle()
print("brand=",car_obj.brand)
print("model=",car_obj.model)
print("color=",car_obj.color)
#constructor (yapıcı,kurucu) metodu
"""
nesne oluşturduğumuz anda otomatik olarak oluşan bir kod var
def _init_(self):   init başlat demek  
  pass
bunu şu şekilde de kullanabiliriz
"""

class vehicle:
    def __init__(self,brand,model,color): #-> selfi class'a ait veriable'lara ulaşmak için kullanıyoruz. self yerine başka bir şey de yazabiliriz  
        self.brand=brand
        self.model=model
        self.color=color
car1_obj=vehicle("skoda","superb","white")
car2_obj=vehicle("honda","civic","green")
print(car1_obj.brand)
print(car2_obj.color)

#------dundar/magic metodları
#constructor özel metodu
class person:
    def __init__(self):
        print("wow! It worked automaically")
p1=person() #fonksiyon çağırılmadan direkt çalışır

#(__str__)-> dışarıya birşey döndürmek  için kullanılır. __ini__'te dışarıya birşey döndüremeyiz.
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def __str__(self):
        return f"Name:{self.name}\nAger:{self.age}"
p1=Person("Sıla",18)
print(p1)

#(__repr__) metodu->kod hakkında daha detaylı bilgi almayı sağlıyor
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def __repr__(self):
        return f"Name:{self.name!r}\nAger:{self.age!r}"
p1=Person("Sıla",18)
print(p1)

#kendi özel metodumuzu oluşturmak
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def My_Info(self):
        print(f"Hello, my name is {self.name}")
        print(f"I am {self.age} years old")
p1=Person("Sıla",18)
p1.My_Info()

#sınıftaki değişkeni dışarıdan değiştirebiliyoruz
p1.age=19
#sınıftaki bir değişkenş del komutuyla silebiliriz
del p1.name

#--------inheritance(kalıtım/miras alma)->başka bir class'ın tüm veriable'larını almamıza olanak sağlar
#en genel class'a parent veya base class, alt class lara da child veya derived class'ı deniliyor

#parent class
class Person:
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
    def  MyPrint(self):
        print(self.firstName,self.lastName)
p1=Person("Sıla","ÇANDIR")
p1.MyPrint()

#child class
class Person:
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
    def  MyPrint(self):
        print(self.firstName,self.lastName)

class Student(Person):  #kullanmak istediğimiz class'ı bu şekilde parametre olarak gönderiyoruz
    pass                #burada pass yazıyor ama person clss'ını çağırdığımmız için onun içindekileri yazdıracak

p1=Student("Sıla","ÇANDIR")
p1.MyPrint()

#eğer parent class'ımızdaki metodumuzun aynısını child class'ında kullanmaya kalkarsak parent metodundaki geçersiz sayılır, onu child da kullanamayız

#super() metodu-> parent classından miras almaya yarıyor
class Student(Person):  
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduationYear=2024 #miras aldığımız calssın dışında ek bir veriable eklemek için kullanıyoruz

#miras alan sınıfa ait metodlar oluşturmak
class Student(Person):  
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduationYear=2024 

    def Welcome(self):
        print(f"welcome {self.firstName} {self.lastName}")

#---------class overriding(metod ezme)
class animal:
    def speak(self):
        return "bark"
class Dog:
    def speak(self):
        return "Hav"

class Cat:
    def speak(self):
        return "Meow"
    
dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())

#-------multiple inheritance(çoklu kalıtım)->bir alt class birden çok üst class'ı miras alabilir.almak istediğimiz classı parametre olarak yazarsak alabiliriz  
#çoklu kalıtımda da method overriding yapılabilir

#bir nesnenin belrli bir class'tan üretilip üretilmediğini kontrol etmek iin isinstance() komutu kullanılabilir
#bir nesnenşn başka bir üst classtan türetilip türetilmediğini kontrol etmek için issubclass() komutu kullanılabilir
  
#----magic(sihirli) metodlar->bizim yazmamıza gerek olmadan oluşturulan metodlar

#__len__ magic metodu ->nesnenin uzunluğunu almak için kullanılır
class customList:
    def __init__(self,items):
        self.items=items
    def __len__(self):
        return len(self.items) 

my_list=customList([1,7,19,12])
print(len(my_list)) 

#__call__ magic metodu ->bir nesneyi fonksiyon gibi çağırmamıza yarar
class Greet:
    def __call__(self,name):
        return f"hello {name}!"
greet=Greet()
print(greet("Sıla"))

#__getitem__->nesneyi list haline çeviriypr

#----------kapsülleme(encapsulation)=erişim belirleyici
#public,protected, private-> bir class içindeli veriable'lara veya metodlara nasıl erişileceğimizi belirliyor
#public-> her yerden erişilebilir demek. kullanmak için bir şey yazmamız gerekmiyor
#protected(_)->sadece class içinden veya miras alan classlar içerisinden erişilebilir. kullanmak için(_) kullanmamız gerekiyor
#private(__)-> sadece tanımlandığı class içerisinden erişilebilir. kullanmak için(__) kullanmamız gerekiyor
#public metodu
class Car:
    def __init__(self,b,m):
        self.brand=b 
        self.model=m
    def display_info(self):
        return f"car:{self.brand} {self.model}"
c1=Car("Skoda","Superb")
print(c1.brand)
print(c1.model)
print(c1.display_info())

#protected(_) metodu
class Animal:
    def __init__(self,n,s):
        self.name=n #public property
        self._species=s #procted  property

    def _makesound(self): #protected method
        return "Animal sound"
class Dog(Animal):
    def __init__(self, n,b):
        super().__init__(n,"Dog")
        self.breed=b
    def display_info(self):
        return f"dog name:{self.name}, breed:{self.breed}, species:{self._species}"
    def make_sound(self):
        return self._makesound()
    
dog=Dog("Kurt","Golden retriver")
print(dog._make_sound)

#private netoduna dışarıdan ulaşamayız sadece oluşturduğumuz class içerisinde kullanabilriz
 
