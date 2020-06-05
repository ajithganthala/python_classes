n = int(input("Enter how many fibonacci series want ot print: "))
a=0
b=1
for i in range(n):
    print(a)
    c=a
    a=b
    b=c+b
