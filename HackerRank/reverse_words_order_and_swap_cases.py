def reverse_words_order_and_swap_cases(sentence):
    word = ""
    words = []
    max = len(sentence)
    l = 0
    # print(sentence)
    for i in range(0,max):
        # print(sentence[i])
        if (sentence[i] ==" "):
            words.append(word)
            # print(word);
            word="";
        if (sentence[i] !=" "):
            word = word + sentence[i]
        l +=1
        if (l == max):
            words.append(word)
            # print(word);
            word="";

    name_list = []
    new_words = words[::-1]
    # print(new_words)
    for i in new_words:
        for j in range(len(i)):
            # print(i[j])
            if i[j].isupper():
                name_list.append(i[j].lower())
            elif i[j].islower():
                name_list.append(i[j].upper())
            else:
                name_list.append(i)
        name_list.append(" ")
    # print(name_list)
    return ''.join(name_list)


print(reverse_words_order_and_swap_cases("aWESOME is cODING EXERSIZE"));