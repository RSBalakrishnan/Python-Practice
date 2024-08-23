# Largest and smallest in a List

li=list(map(int,input("Enter the list Elements :\n(space_separated)").split()))

def finding(arr):
    arr.sort()
    print("Smallest element is ",arr[0],"\nLargest element is ",arr[-1])

finding(li)
