# Given a string ('source') and an array of strings ('negative_words'), find the number of
# appearances of negative words in the source string. Return true if the number is even (e.g. 0, 2,
# 4..) and false otherwise. Note that input strings are case insensitive. If any negative word (e.g.
# 'no') is a substring of another (e.g. ‘not’), count 1.
# even_negatives(source, negative_words)
# even_negatives('Never', ['never']) → False
# even_negatives('Nothing is not mine.', ['nothing', 'Not']) → True
# even_negatives('notyouneverme', ['never', 'Not', 'no']) → True

def even_negatives(source, negative_words):
    count = 0
    for i in range (0, len(negative_words)):
        word = str(negative_words[i]).lower()
        if source.lower().find(word) != -1:
            count += 1
    # print("final count",count)
    if count % 2 == 0:
        return True
    else:
        return False
print(even_negatives('Never', ['never']))
print(even_negatives('Nothing is not mine.', ['nothing', 'Not']))
print(even_negatives('notyouneverme', ['never', 'Not', 'no'])) # shall be False, wrong answer in Example