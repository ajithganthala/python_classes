def evennumbers(a):
    #a = int(input("enter value of a : "))
    #for a in range(1,a+1):
    if (a%2==0):
        return a
#evennumbers()
a = int(input("Enter the number : "))
for i in range(1,a+1):
    print(evennumbers(i),end=" ")
# function with return needs to write print statement
#function without return can be called wihtou a print statement.
"""
def evennumbers():
    a = int(input("enter the number: "))
    for a in range(1,a+1):
        if (a%2==0):
            print("Even numbers are : ",a)

evennumbers()

#HW
#write a function to print fibanaci series

# take a string from user
#strng as habeeb,
#ask user which letter he want to find,print how many times the letter is repeated.

#1HW

def fibanaci_series(a):
    a=
"""
