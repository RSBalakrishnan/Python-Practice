# Reversing the Given List or Array

lss=list(map(int,input("Enter the array values: ").split(' ' or ',')))
lst=list(map(str,lss))

def arrayReverse(a):
    res=''
    for i in a:
        res=i+' '+res
    ls=list(map(int,res.split()))
    print("Reversed list is: ",ls)

arrayReverse(lst)
