# Calculator

while True:
    
    print ("*******************Select Operation******************")
    print ("1.Addition")
    print ("2.Substraction")
    print ("3.Divide")
    print ("4.Multiplication")
    print ("5.Percentage")
    print ("6.Square")
    print ("7.Power")
    print()
    print("**********************************************************")
    print()
    operation=int(input("Enter the selected operation to perform or press '8' to exit 1/2/3/4/5/6/7: "))
    print()
    
    if operation == 8:
        print("good bye")
        exit
        break

    if operation > 7:
        print("invalid")
        exit
        break


    a=int(input("enter the first value: "))
    b=int(input("enter the second value: "))

    if operation == 1:
        print()
        print(a,"+",b,"=",a+b)
        print()
        print("------END, Please Select Another operation to continue or Press 'e' to exit-----")
        print()
        
    elif operation == 2:
        print()
        print(a,"-",b,"=",a-b)
        print()
        print("------END, Please Select Another operation to continue or Press 'e' to exit-----")
        print()
        
    elif operation == 3:
        
        print(a,"/",b,"=",a/b)
        print()
        print("------END, Please Select Another operation to continue or Press 'e' to exit-----")
        print()
        
    elif operation == 4:
        print()
        print(a,"*",b,"=",a*b)
        print()
        print("------END, Please Select Another operation to continue or Press 'e' to exit-----")
        print()
        
    elif operation == 5:
        print()
        print(a,"%",b,"=",a%b)
        print()
        print("------END, Please Select Another operation to continue or Press 'e' to exit-----")
        print()
        
    elif operation == 6:
        print()
        print(a,"**",b,"=",a**b)
        print()
        print("------END, Please Select Another operation to continue or Press 'e' to exit-----")
        print()
        
    elif operation == 7:
        print()
        print(a,"^",b,"=",a^b)
        print()
        print("------END, Please Select Another operation to continue or Press 'e' to exit-----")
        print()
        


