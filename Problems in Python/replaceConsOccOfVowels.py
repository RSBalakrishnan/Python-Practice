s = 'bbaalaakkiibb'

vowels=['a','e','i','o','u','A','E','I','O','U']
ans=s[0]
for i in range(1,len(s)):
    if s[i] != ans[-1] or s[i] == ans[-1] and ans[-1] not in vowels:
        ans+=s[i]

print(ans)
        
    
