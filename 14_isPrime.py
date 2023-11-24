# Defining funtion to chech the given number is Prime or Not
def isPrime(n):
    if(n < 3 and n > 0):
        print(n, "is a Prime number")
    elif(n  ==  0):
        print(n, " is neither or not a Prime")
    else:
        for i in range (2, n):
            if(n%i  ==  0):
                print(n," is Not a Prime number")
                return ()
        print(n, " is a Prime number")

# Getting the number infinitely
while(1):
    num = int(input("Enter a number : "))
    isPrime(num)
