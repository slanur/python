#iç içe fonksiyon kullanımı 
def outer_function(name):
    def greeting():
        return f"hello,{name}"
    return greeting()
print(outer_function("Sıla"))

#decorator->fuction veya metodların işlevselliğini arttırmak için kullanılan yapılardır
#bir projede birçok yerde aynı kod yapısını kullnacaksak bunu kullnabiliriz
#fonksiyonlara dinamik olarak yeni özellikler katmak için kullanırlar
#metod kelimesi nesne programlamada classlar içerisindeki fonksiyonlar için kullanılır

#ihalarda da güvenlik kontrolleri için decorator kullanabiliriz!!!!!!!!

#decorator kullanma örneği
def decoraror_function(func):
    def wrapper_function(*args,**kwargs): #*args ve **kwargs deyimini kaç tane argümanın ve anahtarın kullanılacağının belirsiz olduğu yapılarda kullanırız
        print(f"start")
        result=func(*args,**kwargs)
        print(f"end")
        return result
    return wrapper_function

@decoraror_function
def myMessage():
    print("this is an example function")

myMessage()

#kimlik doğrulama örneği
def authentication(func):
    def wrapper(user,*args,**kwargs):
        if not user.get("auth",False):
            print("authorizatiın failed!")
            return
        return func(user,*args,**kwargs)
    return wrapper

@authentication
def view_account(user):
    print(f"welcome, {user['name']}")

user1={"name":"Sıla Çandır","auth":True}
user2={"name":"Esma Çandır","auth":False}

view_account(user1)
view_account(user2)