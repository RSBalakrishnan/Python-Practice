#Minimum of three numbers :

a=int(input("Enter the number 1: "))
b=int(input("Enter the number 2: "))
c=int(input("Enter the number 3: "))

def mini():
    if a<b:
        if a<c:
            print(a," is the minimum number")
        if a>c:
            print(c," is the minimunm number")
    if b<a:
        if b<c:
            print(b," is the minimum number ")
        if b>c:
            print(c,"i is the  minimum number ")

mini()
