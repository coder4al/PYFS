# Defining funtion to chech the given number is Prime or Not
def isPrime(lst):
    for n in lst:
        if(n < 3 and n > 0):
            primes.append(n)
        elif(n == 0):
            continue
        else:
            for i in range(2, n):
                key = 0
                if(n%i  ==  0):
                    key = 1
                    nPrimes.append(n)
                    break
            if(key == 0):
                    primes.append(n)

# Getting the number infinitely
primes  = []
nPrimes = []

numbersList = [eval(number) for number in (input("Enter the list\t: ").split())]
isPrime(numbersList)

print("Prime numbers\t: ", primes)
print("Not Prime numbers\t: ", nPrimes)
