class BankAccount:
    def __init__(self,a_n,b):
        self.account_number=a_n #public 
        self.__balance=b #private
    
    def Deposite(self,amount):
        if(amount>0):
            self.__balance +=amount
            return f"deposited:${amount}, new balance:{self.__balance}"
        return "Invalid deposit amount"
    
    def __display_balance(self):
        return f"balance:${self.__balance}"
    
    def get_balance(self):
        return self.__display_balance
account=BankAccount("1234567",200)
print(account.Deposite(700))

#---polimorfizm-> bir metodun farklı class larda farklı sonuçlar vermesi
  