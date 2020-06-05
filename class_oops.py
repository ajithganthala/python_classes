#Classes in python

"""class Example: # We have global variable in class
    def test(self): # We have local variables, two combile tow diff kind of variables
        print("From example class test method")

e = Example()
e.test()"""

"""class Gemini:
    def sample(self,a,b):
        print(a+b)
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
e = Gemini()
e.sample(a,b)"""

class Triangle:
    def triangle(self,n):
        #rows = int(input("Enter the numbr of rows : "))
        for a in range(1,rows+1):
            print(" "*(rows-a)+"* "*a)

rows = int(input("Enter the number of rows : "))
e = Triangle()
e.triangle(rows)
