# Duplicates in an Array or List

array=[1,9,8,10,10,10,11,11,12,12,3,4,5,5,5,5,5,5,5,5,5,5]

def duplication(arr):
    dup,uni=[],[]

    for i in array:
        if  i not in uni:
            uni.append(i)
        elif i not in dup:
            dup.append(i)
    print("Duplicated elements are ",dup)

duplication(array)






'''
repeated_array=[]
for i in range(0,len(array)-1):
    
    for j in range(i+1,len(array)):
        
        if array[i]==array[j]:
            if array[i] in repeated_array:
                break
            else:
                repeated_array.append(array[i])
            j=j+1
            
        else:
            j=j+1

print(repeated_array)
'''
