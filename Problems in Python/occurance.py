# Occurance of the Character in a String:

name=str(input("Enter a String : "))
occ=str(input("Enter a Char to find occurance : "))

def occurance(string,char):
    n=0
    for c in string:
        if c==char:
            n+=1
        else:
            continue
    return n

result=occurance(name,occ)
print(f"\nOccurance '{occ}' of the String '{name}' is '{result}'")
