n=int(input("enter the value of n: "))
for a in range (1,n+1):
    for b in range (a,n+1):
        print(" ",end="")    
    for c in range(1,a+1):
        print(c,end=" ")
    print()
    b-=1
    
