#Finding lenght of the list 


def length():
    m=li[-1]
    i=0    
    while li[i]!=m:
        i=i+1
        if li[i]==m:
            print("Lenght of the list is ",i+1)
  
li=[43,9,355]
length()
