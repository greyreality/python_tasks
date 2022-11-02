def solution(s):
    lst = list(s)
    size = len(list(s))
    i, max = 0, 0
    words = 1
    max = 0
    sen = []
    # print(s[size-1])
    for i in range(0, size):
        # print(s[i])
        if s[i] == '.' or s[i] == '?' or i == size - 1 or s[i] == '!':
            print("words=", words)
            print('end------------')
            words = 1
        if s[i] == ' ' and s[i - 1] != '.' and s[i - 1] != '?' and s[i - 1] != '!' \
                and s[i + 1] != ' ' and s[i + 1] != '.' and s[i + 1] != '?' and s[i + 1] != '!':
            words += 1
            # print("space=", words)

        if max < words:
            max = words
    return max


# test = "We test coders. Give us a try?"
test = "?Is is a task!? Forget  CVs... This is a test case! Save time . x x"
print('res=', solution(test))
