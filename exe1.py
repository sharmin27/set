def reverse_words(sentence):
    words =[]
    word =""

    for character in sentence:
        if character ==" ":
            if word:
                words.append(word)
                word =""
        else:
            word += character
    if word:
        words.append(word)
    reversed_sentence=""
    for i in range(len(words) -1,-1,-1):
        reversed_sentence +=words[i] + " "

    return reversed_sentence.strip() #strip function remove space after last word

sentence= "My name is Sharmin"
print(reverse_words(sentence))
