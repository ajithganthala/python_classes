"""class Table:
    def addt (self,a,b):
        print(a+b)

    def multi (self,a,b):
        print(a*b)

    def tablemulti (self,a):
        for c in range(1,11):
            print(a,"*",c,"=",a*c)

a = int(input("Enter tha value of a : "))
b = int(input("Enter tha value of b : "))
e = Table()
e.addt(a,b)
e.multi(a,b)
e.tablemulti(a)"""

class Example:
    n = 'a'
    a = 20
    def __init__(self,name,age): #init is called as constructor.
        self.n=name
        self.a=age
e = Example()
print(e.n,"+",e.a)
