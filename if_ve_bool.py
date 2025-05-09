if 70>7:
    print("First number is greater than second number")

elif 70==7: 
    print("First number and second number are equal")

else:
    print("First number is less than second number")

print(7>4) #bool bir ifade olan true döner

x=70
y=19

if x>y:
    print(x,"is gerater than",y)

x=bool("python") #boş string haric hepsi true olarak döner
y=bool(7) #0 sayısı hariç tüm sayılar true olarak döner
print(x)
print(y)
print(type(x))
print(type(y))
print("bool(""):",bool(""))
print("bool(0):",bool(0))

def myFunction():
    return True
print(myFunction())