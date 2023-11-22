def getOffer(n):
    while(1):
        print("God ", n, "\t: ", end="")
        g = int(input())
        if(g == 7):
            return (g)
        else:
            print("Offering must be 7")

count = int(input("Total lemons : "))

g1 = getOffer(1)
g2 = getOffer(2)
g3 = getOffer(3)

lemons = count - (g1+g2+g3)

if(lemons < 0):
    print("Shortage : ", abs(lemons))
elif(lemons > 0):
    print("Surplus  : ", lemons)
else:
    print("Sufficient..")
    
