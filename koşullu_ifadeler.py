a=7
b=2
#if'i tek satırda yazabiliriz
if(a>b): print("a is greater than b")

#if ve else'nin tek satırda yazımı
print("a is greater than b") if(a>b) else print("a is less than b") 

#if bloğunun içinde and, or, not vs gibi bool veri tiplerini kullanabiliriz

#örnek:notları girilen öğrencinin harf notunu hesaplama örneği(%40 midterm %60 final)
midterm=float(input("enter the midterm grade:")) 
final_exam=float(input("enter the final exam grade:"))
avarage=(midterm*0.4)+(final_exam*0.6)

if(avarage>=90):
    letter_grade="AA"
elif(avarage>=85):
    letter_grade="BA"
elif(avarage>=80):
    letter_grade="BB"
elif(avarage>=75):
    letter_grade="CB"
elif(avarage>=70):
    letter_grade="CC"
elif(avarage>=65):
    letter_grade="DC"    
elif(avarage>=60):
    letter_grade="DD"
elif(avarage>=55):
    letter_grade="FD"
else:
    letter_grade="FF"

print(f"your avarage:{avarage: 1f}")
print(f"your letter grade:{letter_grade}")  

#indirim oranlı kitap sipariş örneği
quantity=int(input("enter the number of books you want to order:")) #miktar
book_price=105
total_price=quantity*book_price

if(quantity>=50):
    discount_rate=0.25 #indirim oranı
elif(quantity>=25):
    discount_rate=0.15
elif(quantity>=10):
    discount_rate=0.10
else:
    discount_rate=0.00
discount_amount=total_price*discount_rate #indirim miktarı

final_price=total_price-discount_amount
print(f"total price(before discount):{total_price:1f} TL")
print(f"discount amount:{discount_amount:1f} TL")
print(f"final price to pay:{final_price:1f} TL")

#örnek:girilen sayının karekökünün tam sayı olup olmadığının kontrolü
my_number=int(input("enter a positive integer number:"))

square_root=(my_number**0.5)
if(square_root==int(square_root)):
    print("the square root is integer")
else:
    print("the square root is not integer") 

#örnek:bir GSM operatörü sabit olarak her ay bizden 50 tl alıyor olsun. 4 dk'ya kadar konuşma ücretsiz iken 4 dk'dan sonra her bir dk için 5 tl ek ücret alıyor.
minutes=int(input("enter the call duration in minutes:"))

fixed_fee=50 #sabit 50 tl ücret
free_minutes=4
extra_fee_per_minutes=5 #ekstra her bir dk'nın ücreti

if(minutes<=free_minutes):
    total_cost=fixed_fee
else:
    total_cost=fixed_fee+(minutes-free_minutes)*extra_fee_per_minutes

print(f"you have to pay:{total_cost}")

#girilen karakter harf mi? harf ise küçük mü büyük mü sesli mi sessiz mi
my_character=str(input("enter a character:"))
 
if(len(my_character)!=1):
 print("please enter only one character")

else:
 if(my_character.isalpha()):
    if(my_character.isupper):
       case="uppercase"
    else:
       case="lowercase"
    vowels="AEIOUaeiou" 
    if(my_character in vowels):
       letter_type="vowel" #sesli harf
    else:
       letter_type="consonant" #sessiz harf    
    print(f"the character '{my_character}' is an {case} {letter_type  }")   
 else:
    print(f"'{my_character}' is not a character")
  
