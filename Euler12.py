#What is the value of the first triangle number to have over five hundred divisors?
#1,3,6,10

import math

#isTriNum was not necessary because it can be incorporated into product 2
def isTriNum(a):
    sum=1
    b=2
    while(sum<a):
        sum+=b
        b+=1
    if (sum==a):
        return True
    else:
        return False
    


def numOfDivisors(y):
    divisor = 0
    for z in range(1, math.floor(y**0.5)+1):
        if( y%z==0):
            divisor+=2
    if (math.floor(y**0.5)==y**0.5):
        divisor -=1
    return divisor


#WHAT DO I MAKE THE RANGE
#OVERLOAD??
def product():
    for i in range(77000000):
        if(isTriNum(i)):
            if(numOfDivisors(i)>499):
                return i


def product2():
    u=1
    inc=2
    while (True):
        if (numOfDivisors(u)>500):
            return u
        else:
            u= u+inc
            inc=inc+1

print(product2())












