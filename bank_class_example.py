class Bankaccount:
    def __init__ (self):
        self.balance=int(input("Enter your Balance "))
    def withdraw(self,amount):
            self.balance-=amount
            return self.balance
            # print("balance = ",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
        #print("balance = ",self.balance)
class AljaziraBank(Bankaccount):
    def __init__(self):
        Bankaccount.__init__(self)
        self.minimum_balance= 2000
        self.max_deposit=10000
    def withdraw(self,amount):
        #print(amount)
        if self.balance-amount<self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            print(Bankaccount.withdraw(self,amount))
    def deposit(self,amount):
        self.amount=amount
        if self.amount > self.max_deposit :
            print("Sorry you exceed daily deposit limitation ")
        else:
            #self.balance+=amount
            print('Your balance after deposit = ' ,Bankaccount.deposit(self,amount))
            #return self.balance
a=AljaziraBank()
a.withdraw(4000)
a.deposit(100001)
