print("hello world")
print('python is so easy') #bu sekilde tek tirnak ile de kullanabiliyoruz 

#print içinde çoklu satır kullanmak
print("""
benim 
adım 
sıla
""")

#veriable
x=7
y="Python"#tek tırnak ile de yazabiliyoruz 
print(x)
print(y) 

x="python programming" #bir değişkenin türünü sonradan değiştirebiliyoruz
print(x)

#pythonda bu şekilde de yazılabilir
x="python programming" ; print(x)
#veriable casting(veri tipini özellikle belirtmek için yapılacak işlem)
z=float(7)
print(z)


#veriable get the type with function
print(type(z))

#veriable unpacking
colors=["white","black","yellow","blue","red"]
a,b,c,d,e=colors
