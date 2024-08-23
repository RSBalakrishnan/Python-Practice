
def noOf(string):
    vows='aeiouAEIOU'
    vow=0
    for i in string:
        if i in vows:
            vow +=1
    print("No of Vowels: ",vow)
    print("No of Consonants:  ",len(string)-vow)

string = input("Enter a string: ")

noOf(string)
    
