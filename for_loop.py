#-------listelerle for kullanımı
fruits=["grape","orange","strawberry","cherry","melon","pineapple","watermelon","apple"]
for item in fruits: #burada fruits içindekiler item'a aktarılır ve tek tek yazdırılır  
    print(item) 

#-----------tuple ile for kullanımı
myNumbers=(70,19,52,41)
for x in myNumbers:
    print(x,end=" ")

#------stringlerle for kullanımı
text="python"
for x in text:
    print(x,end="")

#tek sayıları range metodu ve for kullanarak ekrana yazdırma.örnek, range(0,8) yazdığımızda 0'dan 8'e kadar olan sayılar ekrana yazılır ama 8 dahil değildir
#range metodu kullanımı-> range(start, stop, step)
for x in range(8):
    if(x%2==0):
        continue
    else:
        print(x) 

#girilen sayıya kadar olan çift sayıları bulma
number=int(input("enter a number:"))
for x in range(number):
    if(x%2==0):
        print(x,end=" ") 
        continue
else:
 print("\nloop is over ")

#eğer bir bloğu sonradan doldurmak istiyorsak pass komutunu veya ... yazabiliriz

for x in range(8):
    if(x==4):
        ...
    elif(x==6):
        pass
    else:
        print(x,end=" ")

#nested loop(iç içe döngüler)
adjectives=["red","big","tasty"]
fruits=["grape","orange","strawberry"]

for sıfatlar in adjectives:
    for meyveler in fruits:
        print(sıfatlar,meyveler)

#iç içe listeleri for ile kullanmak
myNumbers=[[70,19],[18,72],[55,52]]

for item1,item2 in myNumbers:
    print(f"{item1},{item2}") 

#hem index numarasını hemde ögeyi almak için enumerate() fonksiyonunu kullanıyoruz 
fruits=["grape","orange","strawberry","cherry","melon","pineapple","watermelon","apple"]
 
for index,item in enumerate(fruits): #ikinci parametre olarak başlangıç değeri girebiliriz 
    print(f"{index}-{item}")

#zip: iki farklı koleksiyonu birleştirerek bir tuple oluşturur
names=["sıla","hakan","esma"]
ages=[18,21,26]
print(list(zip(names,ages))) #[('sıla', 18), ('hakan', 21), ('esma', 26)]

for name,age in zip(names,ages):
    print(f"{index} is {item} age years old")

#örnek:sayı tahmin oyunu
import random
random_number=random.randint(0,100)
score=100 #puan
remaining_attempts=5 #5 deneme hakkı atandı 
i=1

print("you have 5 chance for the know truth")
print(f"your starting score:{score}")
while(i<=5):

    the_entered=int(input("enter a nuber(0-100):"))
    if(the_entered<0 or the_entered>100):
        print("please enter a number between 0-100")
        continue

    remaining_attempts-=1
    if(the_entered>random_number):
        print("enter a less number than your entered!")
        score-=15  
        print(f"your score:{score}")
        print(f"remaining attempts:{remaining_attempts}")
    elif(the_entered<random_number):
        print("enter a bigger number than your entered!")
        score-=15  
        print(f"your score:{score}")
        print(f"remaining attempts:{remaining_attempts}")
    else:
        print("that's true number!")
        print(f"you guessed the number correctly {i}. try")
        print(f"your score:{score}")
        break  
    
    i+=1 
else:
 print(f"the right number is {random_number}")

#örnek:girilen sayının asal olup olmadığını bulma 
entered_number=int(input("enter a number(should be more than 1):"))

if(entered_number<=1):
  print("your entered number should be more than 1")
elif(entered_number==2):
    if(entered_number==2):
     print(f"{entered_number} is prime number")  
else: 
 for i in range(2,entered_number):    
    if(entered_number%i==0):
     print(f"{entered_number} is not prime number")
     break
 else:
  print(f"{entered_number} is a prime number") 
        
#örnek:girilen sayıya kadar olan asal sayıları yazdırma
number=int(input("enter a positive number(should be more than 1):"))
prime_number=[2]
if(number<=1):
    print("the number must be more than 1")
elif(number>=2):
    for i in range(3,number+1,2):  #2 hariç diğer çift sayılar asal olamayacağı için sadece tekleri kontrol ediyoruz
        for j in range(3,i):
            if(i%j==0):
                break
        else:
            prime_number.append(i)
    print(prime_number)

#örnek:obeb okek bulma
number1=int(input("enter the 1. number:"))
number2=int(input("enter the 2. number:"))

smaller=min(number1,number2)
larger=max(number1,number2  )

for i in range(smaller,0,-1): #ebobu bulmak için yazılan döngü
    if(number1%i==0 and number2%i==0):
        gcd=i #ebob
        break

lcd=gcd*(smaller/gcd)*(larger/gcd) #ekok bulma
 
print(f"{number1} and {number2} gcd:{gcd}") #greatest common divisor 
print(f"{number1} and {number2} lcd:{lcd}") #least common multiple

#örnek:fibonacci serisi
fibonacci_size=int(input("enter the fibonacci's size:"))
if(fibonacci_size<=0):
   print("please enter a positive number")
else:
 old_sum=0
 new_sum=1
 for i in range(0,fibonacci_size):
     print(new_sum,end=" ")
     temp=old_sum
     old_sum=new_sum
     new_sum+=temp   

#for döngüsü ile list kullanımı
fruits=["grape","orange","strawberry","cherry","melon","pineapple","watermelon","apple"]
for item in range(len(fruits)): #range(len(fruits)) ile fruitsin uzunluğunu aldık ve item'a boşalttık. 
    print(fruits[item])   #buradada sırayla listin elemanlarını yazdırdık  

#üstteki döngünün farklı bir şekilde kullanılması. bunun adı list comprehension'dur
#[**yeni_deger** for **geçici_değişken** in **liste** if **şart**]
[print(item) for item in fruits]    

#örnwğin listin içindeki ögelerden içinde a harfi geçenleri almak istiyoruz
fruits=["grape","orange","strawberry","cherry","melon","pineapple","watermelon","apple"]
new_list=[]
for item in fruits:
   if("a" in item):
      new_list.append(item)
print(new_list)  
#veya
new_list2=[item2 for item in fruits if("a" in item)]
#list comprehension'un stringle kullanımı
fruits=["grape","orange","strawberry","cherry","melon","pineapple","watermelon","apple"]
new_list2=[item.upper for item in fruits]