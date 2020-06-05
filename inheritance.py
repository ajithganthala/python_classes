#Inheritance

class Animal:
    def example(self,name):
        print(name,"is an amimal")

class Monkey(Animal): #Inheritance
    def exammonkey(self):
        print("Chimpu is not a pet")

class Dog(Animal):
    def examdog(self):
        print("Dog is a loyal pet")

e = Monkey()
e.example("chimpu")
e.exammonkey()
d = Dog()
d.example("Jhonny")
d.examdog()
