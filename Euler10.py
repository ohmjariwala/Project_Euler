
def isPrime(x):
    if (x<2):
        return False
    i=2
    while (i*i <=x):
        if (x%i ==0):
            return False
        i+=1
    return True

def summationOfPrimes(a):
    sum=0
    for i in range (2,a):
        if (isPrime(i)):
            sum+=i
    return sum




print(summationOfPrimes(2000000))