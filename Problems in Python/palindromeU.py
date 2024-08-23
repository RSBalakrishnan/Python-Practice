#  Palindrome in string

string = input("Enter a string : ")

l=len(string)
res=""

for i in string:
    res = i+res

if res == string:
     print('true')
else:
    print('false')



    


