s = 'abghljkm'
n=s[0]

for i in range(1,len(s)):
    if ord(n[-1]) == ord(s[i])-1:
        n+=s[i]
        if i==len(s)-1:
            print(n)
    else:
        if len(n)>1:
            print(n)
        n=s[i]
        
        
