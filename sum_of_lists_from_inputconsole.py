lst1 = []
lst2 = []
lst3 = []

length_lst1=int(input("Enter the length of lst: "))
print()

for a in range(1,length_lst1+1):
    elements_lst=int(input("enter elements for list 1: "))
    lst1.append(elements_lst)
    
print()

for a in range(1,length_lst1+1):
    elements_lst=int(input("enter elements for list 2: "))
    lst2.append(elements_lst)
    
print()

print("elemenst in list 1 is :",lst1)
print()

print("elemenst in list 2 is :",lst2)
print()

for a in range(0,length_lst1):
    elements_lst=lst1[a]+lst2[a]
    lst3.append(elements_lst)

print("the sum of two list is :",lst3)    



      
      
