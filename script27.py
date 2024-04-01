
# bank 
# class level variable - country
# constructor  - fn , ln , accNo transactions
# deposit() , withdrawl()
# static - total accounts
# class level for name change


class Bank:

    country = "India"
    count = 0

    def __init__(self,fn,ln,acc,bal):
        self.firstName = fn 
        self.lastName = ln 
        self.accNo = acc
        self.balance = bal
        self.transactions = []
        Bank.count = Bank.count + 1
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transactions.append(amount)

    def withdrawl(self,amount):
        if(self.balance > amount):
            self.balance  = self.balance - amount
            self.transactions.append(-amount)
        else:
            print("insufficient balance")

    def lastFiveTransaction(self,x):
        return self.transactions[-x::]

    @classmethod
    def changeCountry(cls,cl):
        cls.country  = cl 

    @staticmethod
    def objCount():
        return Bank.count
    
amol  = Bank("amol","rao",123,1000)   
raj  = Bank("raj","rao",123,1000)   
sarika  = Bank("sarika","pansare",123,1000)   
chinmay  = Bank("chinmay","Deshpande",123,10000000)   
poorva  = Bank("poorva","vyas",123,100000000)   

print(Bank.objCount())
amol.withdrawl(1000000000)
amol.deposit(30000000)
amol.deposit(30000)
amol.deposit(3000)
amol.deposit(30)
amol.deposit(3)
print(amol.lastFiveTransaction(2))








