# No. OF VOWELS AND CONSONANTS IN A STRING

string=str(input("Enter a String : "))

def count(string):
    n=len(string)
    m=0
    for char in string:
        if char == 'a' or char=='e' or char=='i' or  char=='o' or char=='u' :
            m+=1
            
    l=n-m
    print(f"No. of Vowels is {m} and\nNo. of consonants is {l}.")

count(string)
