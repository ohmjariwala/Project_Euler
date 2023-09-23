#perfect number: sum of divisors add up to the number
# a number n is called deficient if the sum of its divisors is less than n
# a number n is called abundant if the sum of its divisors exceeds n
#By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from math import floor
from math import sqrt
from math import ceil

def abundantNum(n):
    divisors=0
    limit= ceil(sqrt(n))
    
    for i in range(1,limit):
        if (n % i ==0):
            divisors +=i
            divisors += (n/i)
            
    if (limit **2 ==n):
        divisors +=limit
    
    divisors -= n
    if (divisors > n):
        return True
    else:
        return False

def listAbundantNums():
    l=[]
    for i in range(1, 28123):
        if(abundantNum(i)):
            l.append(i)
    return (l)
             
    
    
    
def product():
    l=listAbundantNums()
    zerolist= [0] * 28123
    for i in (l):
        for j in (l[l.index(i):]):
            summ=i+j
            if (summ <= 28123):
                zerolist[summ-1]= summ
                
    final = 0
    
    for i in range(0,28123):
        if (zerolist[i]==0):
            final +=(i+1)
            
    return (final)

print(product())
                
            
