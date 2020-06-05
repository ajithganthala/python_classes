fruits={"apple":200,
        "banana":50,
        "grapes":100,
        "kiwi":40,
        "prange":10,
        "pineapple":60}
qa={"apple":20,
    "banana":5,
    "grapes":10,
    "kiwi":20,
    "orange":40,
    "pineapple":8}
print("The fruits available are ")
for i,j in fruits.items():
    print(i," :Rs.",j,"Quantity available: ")
buy=[]
qr=[]
t=int(input("How many types of fruits you want to buy from the available : "))
print("Enter the fruits you want to buy and the quantity :")

for i in range(0,t):
    n=input()
    buy.append(n)
    q=int(input())
    qr.append(q)
   
total=0
for i in buy:
    p=fruits[i]
    if qa[i]>0:
        total=total*p
        qa[i]=qa[i]-1
print(total)
m=int(input("Enter the amount: "))
if(m>=total):
    c=m-total
else:
    print("More money is required")
print("Change is :",c)
print(qa)
