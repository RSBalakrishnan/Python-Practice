# [1,1,2,2,2,3]
from collections import Counter

def merasort(nums):
    d={}
    for num in nums:
        if num in d:
            d[num]+=1
        else:
            d[num]=1
    
    print(d)

    nums=[]
    
    
        
            
nums=[1,1,3,2,2,2]

merasort(nums)

