n=0
n=int(input("enter the number of rows: "))
for a in range (0,n):
    for b in range (a,n):
        print(" ", end="")
    for c in range (0,a):
        print ("*",end=" ")
    print()
    b-=1
