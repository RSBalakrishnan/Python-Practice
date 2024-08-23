# Removing Char From a String:

def remowe(c,str1):
    
    stra=list(str1)
    str2=''
    for i in stra:
        if i==c:
            stra.remove(i)
    #print(stra)
    for element in stra:
        str2+=element
    print(str2)
        

b=str(input("Enter The String : "))
a=str(input("Removing Character is : "))
remowe(a,b)



