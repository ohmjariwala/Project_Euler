#Starting in the top left corner of a  2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many routes in a 20x20?

from math import factorial



#binomial coefficient C(a+b,a)
#n= a+b 
def binomial_coefficient(n,k):
    return (factorial(n)/((factorial(k)*factorial(n-k))))
 

print(binomial_coefficient(40,20))


