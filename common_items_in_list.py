lst1 = []
lst2 = []
lst3 = []

length_lst1=int(input("Enter the length of lst: "))
print()

for a in range(1,length_lst1+1):
    elements_lst=input("enter elements for list 1: ")
    lst1.append(elements_lst)
    
print()

for a in range(1,length_lst1+1):
    elements_lst=input("enter elements for list 2: ")
    lst2.append(elements_lst)
    
print()

print("elemenst in list 1 is :",lst1)
print()

print("elemenst in list 2 is :",lst2)
print()

for c in range(0,len(lst1)):
    for b in range(0,len(lst2)):
        if(lst1[c]==lst2[b]):
            for a in range(0,1):
                lst3.append(lst2[b])
print("common in elements in two list are :",lst3)
