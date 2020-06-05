l=int(input("Enter Lenght of traingle "))
w=int(input("Enter width of the traingle "))
for i in range (0,l):
    print("*", end=" ")
print()    
for t in range (1,w):
    for o in range (0,t):
        if (o==1):
            print("*", end="")
            for j in range (1,1+(l-2)):
                print (" ", end="")
            print("*")
for i in range (0,l):
    print("*", end=" ")
