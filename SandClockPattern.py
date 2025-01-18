num = int(input("Enter Any Number : "))
for x in range(num-1):     # Row
    for y in range(x+1):    #Coloumn
        print(" ",end="")
    for z in range(num-x):
        print("*",end="")
    for v in range(num-x-1):
        print("*",end="")
    print()
for x in range(num):     # Row
    for y in range(num-x):    #Coloumn
        print(" ",end="")
    for z in range(x+1):
        print("*",end="")
    for v in range(x):
        print("*",end="")
    print()
