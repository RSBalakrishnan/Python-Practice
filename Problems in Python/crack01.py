def myFunc(a,b=15,*args):
    print(a)
    print(b)
    print(args)
    return a+b+sum(args)
    
result=myFunc(1,0,3,4,5)
print(result)

