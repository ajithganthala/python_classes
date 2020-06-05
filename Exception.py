a =10
try:
    b = (a/0)
    print(b)
except:
    print("a divisible by zero gives infinity")
finally:
    print("Hai")
