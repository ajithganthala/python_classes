n=int(input("Enter a number : "))
a=1
b=1
c=1
p=n
while (a<=n):
    while (b<=p):
        print(" ",end="")
        b+=1
    while (c<=a):
        print("*",end=" ")
        c+=1
    print()
    p-=1
    a+=1
    b=1
    c=1
