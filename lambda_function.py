#lambda ile bazı fonksiyonları kısa bir şekilde oluşturabiliriz

result= lambda x: x+10
print(result(9))

def get_square(x):
    return x**2
get_square=lambda x: x**2 #üstteki fonksiyonun kısaltılmışı  
print(get_square(9))

#lambda birden fazla argüman alabilir
sum=lambda x,y,z: x+y+z
print(sum(2,3,4))
  
#koşullu ifadelerle lambda kullanımı
check_the_sign=lambda x: "positive" if(x>0) else "negative"
print(check_the_sign(-1))

#list tuple vs'lerde lambda kullanımı
#map(),filter() ve sort() metodu

#map()->list,tuple gibi iterable'lara fonksiyın uygulamak için kullanılıyor  
numbers=[1,2,3]
result=map(lambda x:x*2,numbers)
print(list(result))

#birden fazla listeyi lambda fonksiyonunda kullanmak 
list1=[1,2,3]
list2=[4,5,6]
result=map(lambda x,y:x+y,list1,list2)
print(list(result))
 
#map ve lambda fonksiyonu ile koşullu ifade kullanımı
numbers=[7,4,19,12]
result=map(lambda x: "even" if(x%2==0) else "odd",numbers)
print(list(result)) 

#filter()->bir iterable'daki elemanları bir koşula göre filtrelemeye denir
numbers=[7,4,19,12,5,90]
result=filter(lambda x:x%2!=0 ,numbers)

print(list(result)) 

#sorted()->orijinal iterableye dokunmadan soralanmış bir kopyasını döndüren fonksiyon.
#sorted(iterable,key=None,reverse=False)
numbers=[4,1,3,2]
result=sorted(numbers)

#lambda ile kullanımı
numbers=[4,-6,1,3,-5,2]
result=sorted(numbers,key=lambda x:abs(x)) # tüm sayışarı pozitif yapıp öyle sıralar  

#normal fonksiyonun içinde lambda kullanmak
def myFunction(n):
    return lambda x:x*n
result=myFunction(5)
print(result(9))
