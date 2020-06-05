# Pattern by using nested for loop
"""rows = int(input("Enter the number of rows: "))
for a in range(rows):
    for b in range(rows):
        print("*",end=" ")
    print()"""

 ### Pattern programs without usong nested for loop, by using SPACING program.###

#pattern without nested (WN) for loop(right angled traingle)

"""rows = int(input("Enter the numbr of rows : "))
for a in range(1,rows+1):
    print(" "*(rows-a)+"*"*a)"""


#Pattern WN for loop (90 angled traingle)

rows = int(input("Enter the numbr of rows : "))
for a in range(1,rows+1):
    print(" "*(rows-a)+"* "*a)

#Pattern WN for left angled traingle

"""rows = int(input("Enter the number of rows: "))
for a in range(1,rows+1):
    print("  "*(rows-a)+"* "*a)"""

#Pattern WN for inverted left angled traingle

"""rows = int(input("Enter the number of rows: "))
for a in range(rows,0,-1):
    print("  "*(rows-a)+"* "*a)"""
    
#Pattern WN for invrted right angled traingle

"""rows = int(input("Enter the number of rows: "))
for a in range(rows,0,-1):
    print("* "*a)"""

#Pattern WN Diamond shape

"""rows = int(input("Enter the number of rows: "))
for a in range(1,rows+1):
    print(" "*(rows-a)+"* "*a)
for a in range(rows-1,0,-1):
    print(" "*(rows-a)+"* "*a)"""

#Pattern WN for arrow shape

"""rows = int(input("Enter the number of rows: "))
for a in range(1,rows+1):
    print("* "*a)
for a in range(rows-1,0,-1):
    print("* "*a)"""

#Pattern WN for inverted arrow shape

"""rows = int(input("Enter the number of rows: "))
for a in range(1,rows+1):
    print("  "*(rows-a)+"* "*a)
for a in range(rows-1,0,-1):
    print("  "*(rows-a)+"* "*a)"""



    
