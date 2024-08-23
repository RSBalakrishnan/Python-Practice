#Check Whether The Given String is Paliindrome or Not

def CheckPalindrome(a,b):
    if a==b:
        print("Yes it is Palindrome .")
    else :
        print("It is Not Palindrome")
    

str1=str(input("Give Some String to check Palindrome : "))

str2=str1.upper()
str3=''.join(reversed(str2))

CheckPalindrome(str2,str3)








    
