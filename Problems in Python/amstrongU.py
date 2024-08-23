#prints Amstromg numbers between some ranges

for i in range(1001):
    num=i
    res = 0
    n=len(str(i))
    while(i!=0):
        k=i%10
        res=res+k**n
        i=i//10

    if num == res :
        print(num)
        
        
        
