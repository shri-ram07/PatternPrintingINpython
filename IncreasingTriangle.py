num = int(input("Enter Any Number : "))

for x in range(num):     # Row
    for y in range(x+1):    #Coloumn
        print("*",end="")
    print()