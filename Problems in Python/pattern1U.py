

n=int(input("Enter n value: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print("\n")
        
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end='')
    
print("\n\n")

for i in range(1,n+1):
    print(i*'*',end='')
    print("\n")

print("\n\n")

for i in range(1,n+1):
    if i==1 or i==n:
        print(i*'*',end='')
    else:
        print("*",(i-1)*' ','*',end='')
    print("\n")
