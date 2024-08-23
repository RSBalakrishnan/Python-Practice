# Occurance of a string

def occurance(string,which):
    count =0
    for i in string:
        if i ==which:
            count +=1
        else:
            continue
    print(count)

string = input("Enter a string: ")
which =  input("Occurance of : ")

occurance(string,which)
