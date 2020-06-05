shp_list=['Milk', 'Bread','Eggs','Jam','Biscuits','Soap','Shampoo','Rise','Flour','Jouce']
#code={'Milk':233, 'Bread':740,'Eggs':154,'Jam':195,'Biscuits':801,'Soap':560,'Shampoo':264,'Rise':295,'Flour':830,'Jouce':550,'Yoghout':456,'Meat':123}
prices={'Milk':23, 'Bread':40,'Eggs':5,'Jam':105,'Biscuits':80,'Soap':20,'Shampoo':200,'Rise':25,'Flour':30,'Jouce':50,'Yoghout':44,'Meat':300}
stock={'Milk':229, 'Bread':140,'Eggs':1115,'Jam':165,'Biscuits':1803,'Soap':1220,'Shampoo':220,'Rise':125,'Flour':130,'Jouce':150,'Yoghout':444,'Meat':120}
total=0
total_bill=0
print("Enter the items :")
for i in shp_list:
    item= i
    Bill=prices[i]
    print(item,',' ,end=' ')
    amount=int(input((" Quantity ")))
    print (i," : ",Bill," * ", amount," = ",Bill*amount)
    total=total+Bill*amount
    stock[i]=stock[i]-amount
print()    
print('            ***************************            ')
print()
print('Your Bill is =  ',total)
print()    
print('            ***************************            ')
print()
cstmr_pay=int(input(("Customer payment = ")))
print()    
print('            ***************************            ')
print()
print('Customer change = ' ,cstmr_pay-total)
print(stock)
