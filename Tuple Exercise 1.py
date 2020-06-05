shopping = ['apple phone','samsung','nokia']
stock = {'apple phone' : 10, 'samsung' : 15, 'nokia' : 12, 'oppo' : 20}
prices = {'apple phone' : 60000, 'samsung' : 12000, 'nokia' : 25000, 'oppo' : 6000}
total = 0

s = shopping
st = stock
ps = prices
t = total

for i in s:
    p= ps[i] #p = price
    if st[i]>0:
        t =t +p
        st[i]=st[i] -1

print("total purchase value is :",t)
print("The available stock is : ",st)


