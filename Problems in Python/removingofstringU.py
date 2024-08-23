#String removing

def removing(string,rem):
    res=""

    for i in string:
        if i != rem:
            res += i
        else:
            continue

    print("Final output is "+res)


string=input("Enter a string : ")
rem = input("Removing string is : ")

removing(string,rem)
        
