from abc import ABC ,abstractmethod
class Box(ABC):
    @abstractmethod
    def addt(self,items):
        pass
    @abstractmethod
    def emptyt (self):
        pass
    @abstractmethod
    def countt (self):
        pass
class Item (Box):
    def __init__ (self,name,value):
        self.name= name 
        self.value= value 
    def addt (self,items):
        self.items=self.name
        print(self.items)
    def emptyt (self):
        pass
    def countt (self):
        pass
class List(Box):
    def __init__ (self):
        self.count=0
        self.items=[]
    def addt (self,items):
        self.new_items=[]
        for i in range (0,items):
            list2=input("Enter item to add into list:  ")
            self.items.append(list2)
            print()
        print("The items in the list are: ",self.items)
        print()
        self.new_items=self.items
    def emptyt (self):
        
        pass
    
    def countt (self):
        for i in  self.new_items:
            self.count+=1
        print("The no.of items in the list is : ",self.count)
        print("-------------------------------------------------------------------------")
class Dictionary (Box):  
    def __init__ (self):
        self.items={}
        self.count=0
    def addt (self,items):      
        for i in range (0,items):
            print()
            self.items[i]=input("Enter Item the item to add into dictionary : " )
            print()
        print("The number of items in dictionary is : ",self.items)
        print()
        self.new_items=self.items
    def emptyt (self):
        pass
    print()
    def countt (self):
        for i in self.items:
            self.count+=1
        print ("The count in Dictionary is : " ,self.count )
        print()
a = Item('Groceries',10)
b =List()
d = Dictionary()
c = int(input("Enter qauntity of items to add in the list : "))
print()
b.addt(c)
b.emptyt()
b.countt()
e = int(input("Enter number of items to add in dictonary : "))
print()
d.addt(e)
d.emptyt()
d.countt()
