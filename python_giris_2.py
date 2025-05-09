#output veriables 
x="Python"
y="is"
z="wonderful"
print(x,y,z)

#veya
print(x+y+z)

print("pi",3.14,sep="->")
 
#
a=5
b=7
print(a+b) # + işareti hem matematiksel işlemlerde hemde metinsel ifadeleri birleştirmede kullanılır 
#ama bir sayıyı ve bir metinsel ifadeyi '+' işaretiyle birleştiremeyiz

#global veriables
text="maervellous"

def my_function():
   print("Python is "+text)

my_function()


#local veriables
def my_function():
   text="fantastic"     #fonksiyonun içinde global önsözcüğünü kullanarak global değişken oluşturabiliriz 
   print("Python is "+text)
my_function() 
print("Python is "+text)
