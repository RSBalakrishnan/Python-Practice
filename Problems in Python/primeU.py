

def isprime(n):
    for i in range(1,n+1):
        if i<=1:
            print(False,i)
        elif i==2 or i==3:
            print(True,i)
        elif i>3:
            le=int((i**0.5)+1)
            
            for j in range(2,le):
                if i%j ==0:
                    state=False
                    break
                else:
                    state=True
                    continue
            if state==True:
                print(True,i)
           # else:
               # print(False,i)



isprime(50)




        
