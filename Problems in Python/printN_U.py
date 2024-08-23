
def printN(n):
    if n==0:
        return
    print(n)
    printN(n-1)
    


n=5
printN(n)
