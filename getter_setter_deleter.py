#getter, setter ve deleter methodları
#class'ın bir methodunu veriable gibi kullnamamıza olanak sağlar

#getter dışarıya birşey döndürmek için kullanılır
#setter içeriğini değiştirmek için kullanılır

class Person:
    def __init__(self,name):
        self._name=name

    @property
    def name_function(self): #getter methodu
        return self._name
    
    @name_function.setter
    def name_function(self,new_name):#setter methodu
        if not new_name:
            raise ValueError("Name cannot be empty1!!") #bu şekilde bir uyarı gönderebiliriz
        self._name=new_name
    @name_function.deleter
    def name_function(self): #deleter methodu
        print("deleting name veriable...")
        self._name=None 

p1=Person("Sıla")
print(p1.name_function) #normalde fonksiyonları çağırırken boş parantez koyardık ama bu methodla veriable gibi çağırabiliyoruz
del p1.name_function 