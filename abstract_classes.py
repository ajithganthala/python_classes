"""import keyword
#print(keyword.kwlist)
print(type(1))
print(type([]))
print(type({}))
print(type(()))
print(type(""))
print(type(keyword)) #module is class"""

#Extending properties of super calss into sub class is called as inheritance
#Forcing to use same function which is defined in super class

# @ is called as annotation for any method
#abstract method  class example
"""from abc import ABC,abstractmethod #ABC is abstract base class

class Bankclass(ABC):
    @abstractmethod # we can write @ for what function we need to abstract
    def deposit(self,amount):
        pass
class AndhraBank(Bankclass):
    def example(self):
        print("hi")
    def deposit(self,amount):
        print(amount)
        
e = AndhraBank()"""

from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def walks(self,name):
        pass
class monkey(animal):
    def walks(self,name):
        print(name,"Walks on four legs")
class dog(animal):
    def walks(self,name):
        print("Dog is loyal pet")

e = monkey()
#w = input("Enter the animal name: ")
e.walks('k')

"""f = dog()
k = input("Enter your pet name: ")
f.walks(k)"""
 



    
