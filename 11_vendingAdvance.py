coin  = int(input("Enter coins : "))
count = int(input("Enter count : "))

coin -= count

if(count <= 5):
    for i in range (count):
        print("Take your pepsi..")
elif(count > 5):
    for i in range (1, 6):
        print("Take your pepsi..")
    print("Out of stock")
print("Have a nice drink..")
