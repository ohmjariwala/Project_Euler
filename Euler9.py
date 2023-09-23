#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
from math import floor

def abc1000():
    #Check what values make a + b + c = 1000
    #a<b<c
    for a in range (floor(1000/3)):
        for b in range (a, floor((1000/2))):
            c= 1000- a- b
            if (a**2 + b**2 ==c**2):
                return(a*b*c)

def abcNoRange():
    for a in range(1, 1000):
        for b in range(a,1000):
            c=1000-a-b
            if(a**2 + b**2 ==c**2):
                return (a*b*c)

print(abc1000())
print(abcNoRange())