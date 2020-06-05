class Bank_Account:
    def __init__ (self):
        self.balance=int(input("Enter the balance to add into your account: "))
    def withdraw(self,withdrawamount):
        self.balance = self.balance-withdrawamount
        print("Available amount is : ",self.balance)
    def deposit(self,depositamount):
        self.balance = self.balance+depositamount
        print("Balance is: ",self.balance)

class HDFC_Bank(Bank_Account):
    def __init__(self):
        Bank_Account. __init__ (self)
        self.m_balance=5000
        self.max_depositamount=10000

    def withdraw(self,withdrawamount):
        if self.balance - withdrawamount <= self.m_balance:
            print("Minimum balance of '5000' must be maintained")
        else:
            print(Bank_Account.withdraw(self, withdrawamount))
            
    def deposit(self,depositamount):
        self.depositamount=depositamount
        if self.depositamount > self.max_depositamount :
            print("Sorry you exceed daily deposit limitation ")
        else:
            print(Bank_Account.deposit(self,depositamount))
            

e = HDFC_Bank()
n = int(input("Enter the amount to withdraw: "))
e.withdraw(n)
d = float(input("Enter the amount to deposit: "))
e.deposit(d)

"""d = HDFC_Bank(10000)
a = int(input("Enter the amount to deposit: "))
d.deposit(a)"""
        

"""e =Bank_Account()
n = int(input("Enter the amount to deposit: "))
e.deposit(n)
w = int(input("Enter the amount to withdraw: "))
e.withdraw(w)"""
