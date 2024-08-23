# Longest word inn sentence

def longest(sen):
    j=0
    for i in sen:
        if len(i) > j:
            j=len(i)
            word=i
        else:
            continue
    print("Longest word is ",word)

#sen=list(map(str,input("Enter a sentence: ").split()))

sen2=input("Enter a sentence: ")

sen3=[]
word1=""
for j in sen2:
    
    if j!=' ':
        word1 += j
    else:
        print(word1,end=' n ')
        word1=""
        
#print(sen3)       
        

#longest(sen3)
