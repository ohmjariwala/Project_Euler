#n --> n/2 if n is even
#n--> 3n+1 if n is odd
#Which starting number, under one million, produces the longest chain?

def collatzSeq(x):
    if x==1:
        return 1
    if x%2 ==0:
        x= x/2
        return 1 + collatzSeq(x)
    else:
        x= (3*x)+1
        return 1+ collatzSeq(x)

def longest_sequence():
    current_max_count=0
    for i in range(1,1000000):
        count= collatzSeq(i)
        if count>current_max_count:
            current_max_count=count
            print (i, count)


print (longest_sequence())
        

