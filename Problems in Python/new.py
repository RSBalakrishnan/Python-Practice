def cons(lst:list)->bool:
    a,i=lst[0],0

    while i<len(lst):
        if lst[i]!=a:
            return False
        i+=1
        a+=1
    return True

num=[3,4,5,6,7,8,9]
num2=[2,3,5,6,9,10]

#print("\n",cons(num),"\n",cons(num2))

# Fibonacci
def fibo(n):

    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo(n-2) + fibo(n-1)

#print(fibo(6))

def fiboSeries(n):

    seq=[0,1]

    while len(seq)<n:
        nex=seq[-2]+seq[-1]

        seq.append(nex)
    return seq

#print(fiboSeries(7))
        
def sortstr(s):
    se=s
    for i in range(len(se)):
        for j in range(i,len(se)):
            if s[i]>s[j]:
                temp=s[i]
                s[i]=s[j]
                s[j]=temp

    return se


s=[3,4432,43,23,43,12,5,65]
print(sortstr(s))                
        

def anagram(s1,s2):
    dic1={}
    dic2={}
    for c in s1:
        if c in dic1:
            dic1[c]+=1
        else:
            dic1[c]=1
    for c in s2:
        if c in dic2:
            dic2[c]+=1
        else:
            dic2[c]=1
 
            
    return dic1==dic2

s1='silent'
s2='liten'

#print(anagram(s1,s2))
    
        







































    
