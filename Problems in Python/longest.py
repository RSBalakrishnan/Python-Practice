# Longest word in a given sentence:

sent=str(input("Write a Sentence : "))


def longest(sentence):
    
    list1=sentence.split(' ')

    for c in list1:
        n=len(c)
        m=0
        if n>m:
            m=n
            maxx=c
        elif n<m:
            continue
    print("Longesr word in the Sentence is ",maxx,"having the count of ",m)
            
longest(sent)
