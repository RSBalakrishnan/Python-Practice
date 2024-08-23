j=int(input("how many elements you want to print; "))


li=[]

for i in range(0,j):
        ke=int(input("Enter the elements of list; "))
        li.append(ke)
print("Enterd liat is",li)

print("INTER CHANGING THE LIST ")

li[0],li[-1]=li[-1],li[0]
print("IC list is ",li)

