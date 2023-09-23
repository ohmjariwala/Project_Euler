from math import factorial

value= str((factorial(100)))

sum=0
for i in range(len(value)):
    sum+= int(value[i])

print(sum)