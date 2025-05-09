i=0
while(i<5):
    print("python")
    i+=1

i=0
while(i<5):
    print(i,end="  ")#eğer yan yana yazdırmak istiyorsak bunu kullanıyoruz
    i+=1
#brak ve continue komutu aynı 

#döngü sonunda else komutu kullanmak
i=1
while(i<=7):
    print(i,end=" ")
    i+=1
else:
    print(f"\ni({i}) veriable is no longer less than 7")
print("while loop was over")
#ama döngü içinden break komutuyla çıkılmışsa else'i bu şekilde kullanmaya izin vermiyor

#listlerle döngü kullanımı
myNumbers=[19,7,32,52,27]

i=0
while(i<len(myNumbers)):
    print(myNumbers[i])
    i+=1  

#örnek: kullanıcıdan alınan 7 sayıyı ekrana yazdırma
myNumbers=[]
i=0
while(i<7):
    input_number=int(input("enter an inetger:"))
    myNumbers.append(input_number) #list'e eleman eklemek için
    i+=1
myNumbers.sort() #list'i küçükten büyüğe   sıralamak için  
print(myNumbers)

#örnek:girilen sayıya kadar olan tek ve çift sayıları yazdıran program
tek_sayilar=[]
cift_sayilar=[]
first_number=int(input("ilk sayıyı giriniz:"))
last_number=int(input("son sayıyı giriniz:"))

while(first_number<last_number):
    if(first_number%2==0):
        tek_sayilar.append(first_number)
    else:
        cift_sayilar.append(first_number)
    first_number+=1

print("tek sayilar=",tek_sayilar)
print("cift sayilar=",cift_sayilar)

#örnek:kullanıcıdan bir isim girilene kadar isim iste
while   (True):
    name=input("enter your name:")
    if(name==""): #isspace, stringin hepsi boşluktan oluşuyorsa true döndürüyor
        continue
    else:
        break
print(f"your name is: {name}")

#örnek:faktöriyel hesaplayan program
number=int(input("enter a number:"))

factoriel=1
while(number>0):
    factoriel*=number
    number-=1
print(f"{number}!={factoriel}") 
