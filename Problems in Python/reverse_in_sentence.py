# Reverse words in a sentence

input_sentence=str(input("Enter a sentence : "))

def reversing(sentence):

    sentence_to_list=[word[::-1] for word in sentence.split()]

    #answer=' '.join(sentence_to_list)
    answer=''
    for word in sentence_to_list:
        answer += word+' '
        
    return answer
        
result=reversing(input_sentence)
print("Reversed sentence is ,",result)


