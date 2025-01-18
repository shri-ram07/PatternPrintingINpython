num = int(input("Enter Any Number : "))

for x in range(num):     # Row
    for y in range(num-x):    #Coloumn
        print("*",end="")
    print()