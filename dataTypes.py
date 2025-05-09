
# c'den farklı veriable türleri
comp=2j #complex data type. complex sayiları başka bir sayı türünw dönüştüremeyiz

myList=["Apple","Grape","Banana","watermelon"] #list data type  
print(myList)
myTupel=("Apple","Grape","Banana","watermelon") #tuple data type. Tupl'nın list'ten farkı elemanlarının değiştirilememesi

myRange=range(7) #range data type. Range 0'dan 7'ye kadar sayı dizisi tanımlar. print(*myRange) şeklinde yazdırılır

myDict={"name":"Sila","age":18}#dict içinde  birden fazla veriyi tutmamıza izin veriyor, anahtar değer çifti olarak geçiyor genelde

mySet={"Apple","Grape","Banana","watermelon"} # set data type

myFrozenSet=frozenset({"Apple","Grape","Banana","watermelon"}) #frozenset data type

myBool=True # bool data type. sadece true veya false değerini alır 

#None data type. C'deki NULL ifadesine denk gelir

import sys
x=7
print(sys.getsizeof(x)) #veriable'nın boyutuna ulaşabilmek için bunu kullanıyoruz

x=str("hello python") # bu şekilde özel olarak veriable tanımlaması da yapabiliyoruz
y=str(True) # burada true artık boolean bir ifade değil bir string ifadedir

z=complex(2,3) # çıktı olarak 2+3j ifadesini verir

w=19E4  # bunun anlamı 19*(10 üzeri 4)

#Python'da dir() komutu, bir nesnenin özniteliklerini (attributes) ve metotlarını (methods) listeleyen yerleşik (built-in) bir fonksiyondur