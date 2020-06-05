
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("enter value of c: "))
d = int(input("enter value of d: "))
if (a>(b and c and d)):
        print(a,"is greater than",b,c,d)
elif (b>(a and c and d)):
        print(b,"is bigger than",a,c,d)
elif (c>(a and b and d)):
        print(c,"is bigger than",a,b,d)
else:
        print(d,"is bigger than",a,b,c)

"""for i in range(1,11):
        print(i,end= ",")"""
        
