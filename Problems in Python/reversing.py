# Reversing a String

string=str(input("Enter a String : "))

def reversing(string):

    rev=''
    for char in string:
        rev=char+rev

    print("\nBy string inbuilt function ",string[::-1])
    return rev

result=reversing(string)
print(f"\nReversed string of '{string}' is '{result}' .")
