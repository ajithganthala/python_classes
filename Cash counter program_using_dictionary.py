## Cash Counter program
while True:
    
    print("------------------Welcome to fresh fruits zone--------------------")
    print()
    print("...................................................................")
    print()
    print("Here are your Available fruits are : ")
    print()
    print("...................................................................")
    print()
    print("0.Apple")
    print("1.Guava")
    print("2.Mango")
    print("3.Pine Apple")
    print("4.Jack Fruit")
    print("5.Black Garpe")
    print("6.White Grape")
    print("7.Blue Berry")
    print("8.Water Melon")
    print("9.Sweet Orange")
    print("10.Orange")
    print("11.black berry")
    print("...................................................................")
    print()

    print("The Prices of fruits are :")
    print()
    itemsprice = ['Apple: 60 rs','Guava: 5 rs','Mango: 80 rs','Pine Apple: 30 rs','Jack Fruit: 30 rs','Black Grape kg : 25 rs','White Grape kg :60 rs','Blue Berry: 80 rs','Water Melon: 40 rs','Sweet Orange: 20 rs','Orange: 20rs','black berry: 10 rs']

    for price in range(0,len(itemsprice)):
        print("Price of fruit: ",itemsprice[price])
    print()
    print("...................................................................")
    print()

    print("The Quantities of fruits are :")
    print()
    Quantity = ['Apple: 10 pcs','Guava: 20 pcs','Mango: 40 pcs','Pine Apple: 45pcs','Jack Fruit :50 pcs','Black Grape: 55 kg','White Grape: 15 kg','Blue Berry: 25 pcs','Water Melon: 5 pcs','Sweet Orange: 15 pcs','Orange: 10 pcs','black berry: 25 pcs']

    for qa in range(0,len(Quantity)):
        print("Quantity of fruit: ",Quantity[qa])
    print()
    print("...................................................................")
    print()

    items = ['Apple','Guava','Mango','Pine Apple','Jack Fruit','Black Grape','White Grape','Blue Berry','Water Melon','Sweet Orange','Orange','black berry']
    stock = {'Apple':10,'Guava':20 ,'Mango':40 ,'Pine Apple':45 ,'Jack Fruit':50 ,'Black Grape':55 ,'White Grape':15 ,'Blue Berry':25 ,'Water Melon':5 ,'Sweet Orange':15 ,'Orange':10 ,'black berry':25}
    prices = {'Apple':60,'Guava':5,'Mango':80,'Pine Apple':30,'Jack Fruit':30,'Black Grape':25,'White Grape':60,'Blue Berry':80,'Water Melon':40,'Sweet Orange':20,'Orange':20,'black berry':10}
    #total = 0
    total_bill = []
    cart = []
    qr = []
    
    
    it = items
    #t = total
    st = stock
    pr = prices
    tb = total_bill
    c = cart
    
    choice = input("Please press 's' purchase or press any 'key' to exit : ")

    if choice == 's':
         
        t = int(input("enter how many kinds of fruits want to buy : "))
        print()
        for i in range(0,t):
            n=input("Enter the fruit name as per displayed : ",)
            c.append(n)
            q=int(input("Enter the quantity of fruit: "))
            print()
            qr.append(q)

        total=0
        t = total
        for i in c:
            p=pr[i]
            if st[i]>0:
                t=t+p*q
                st[i]=st[i]-q
        print()
        print("...................................................................")
        print()
        print("the total cart value is :",t)
        print()
        print("...................................................................")
        print()
        m=int(input("Enter the amount: "))
        if(m>=t):
            c=m-t
        else:
            print("More money is required")
        print()
        print("...................................................................")
        print()
        print("Money return is :",c)
        print()
        print("...................................................................")
        print()
        print("The available stock is: ",st)
        print()
        print(".....................THANK YOU VISIT US AGAIN..............................................")
        print()

    exit
    break

    if choice == 'e':
        exit
        break


   
