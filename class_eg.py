# pip (python package index) it is used to import from diffferent locations

class Mlti_Table:
    def mltitable(self,n):
        for i in range(1,11):
            print(n,"*",i,"=",n*i)

class Triangle:
    def triangle(self,rows):
        #rows = int(input("Enter the numbr of rows : "))
        for a in range(1,rows+1):
            print(" "*(rows-a)+"* "*a)

class Example:
    def __init__ (self,name,age):
        self.n = name
        self.a = age
        
    def printdata(self):
        print(self.n,self.a)

e = Example('ajith',20)
e.printdata()
m = Mlti_Table()
m.mltitable(5)             
