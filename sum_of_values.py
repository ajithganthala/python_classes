# defining and returning the function

def sumoftwo():
    a = int(input("Enter the first number : "))
    b = int(input("Enter the Secon number : "))
    return a+b

print(sumoftwo())

"""def primenumbers():
    a = int(input("Enter how many number you want : "))
    x=0
    for j in range(1,a+1):
        for i in range(1,j+1):
            if (j%i==0):
                x+=1

        if (x<=2):
            print(j,end=" ")
        x=0
primenumbers()"""
