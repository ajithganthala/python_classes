#find the biggest number in the given list and find the smallest number and print smallest number in right angles triangle.
"""a = [-1,-2,10,11,3,4,-8,0,1,2,5,7]
b = a[0]
c = a[0]
for k in range(1,len(a)):
        if(b>a[k]):
         b = a[k]
        if(c<a[k]):
         c = a[k]
print("the smallest number is: ",b)
print("the biggest number is: ",c)

for i in range(0,c+1):
    for j in range(0,i):
        print(b,end=" ")
    print()"""

# sorting the number without using sort function in list.

a = [-1,-2,10,11,3,4,-8,0,1,2,5,7]
b = a[0]
for i in range(0,len(a)):
    if (b>a[i]):
        b = a[i]
    b.append(a[i])
    a.remove(a[i])
print(c)
    
            
        
