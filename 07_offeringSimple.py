count = int(input("Total lemons : "))
g1 = int(input("God 1 : "))
g2 = int(input("God 2 : "))
g3 = int(input("God 3 : "))

lemons = count - (g1+g2+g3)

if(lemons < 0):
    print("Shortage : ", abs(lemons))
elif(lemons > 0):
    print("Surplus  : ", lemons)
else:
    print("Sufficient..")
    
