

def occurance(string,a):
    count=0
    a1=a.lower()
    string1=string.lower()
    for i in string1:
        if a1==i:
            count+=1
    return count


string="Balakrishnan"
a='A'

#print(occurance(string,a))
for i in range(9850,9950):
    print(i,chr(i))



    
    
