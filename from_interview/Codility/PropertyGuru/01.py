#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Task:
# You would like to find the sentence containing the largest number of words in
# some given text. The text is specified as a string S consisting of N
# characters: letters, spaces, dots(.), question marks(?) and exclamation
# marks (!).
# The text can be divided into sentences by splitting it at dots, question marks
# and exclamation marks. A sentence can be divided into words by splitting it
# at spaces. A sentence without words is valid, but a valid word must contain
# at least one letter
# For example, given S = "We test coders. Give us a try?", there are three
# sentences: "We test coders","Give us a try" and "". The first sentence
# contains three words:"We","test", "coders". The second sentence
# contains four words: "Give","us","a","try". The third sentence is empty.
# Write a function that, given a string A consisting of N characters, returns the maximum
# number of words in a sentence.
# For example S = "We test coders. Give us a try?", the function should return 4, as explained.
# For example S= "Forget CVs..Save time . x x" should return 2,
# as there are four sentences:"Forget CVs"(2 words), ""(0 words),
# "Save time"(2 words) and " x x" (2 words)
# Focus on correctness not on performance

# TODO: to check case with a string with two spaces
def solution(s):
    size = len(list(s))
    words = 1
    max = 0
    # print(s[size-1])
    for i in range(0, size):
        if s[i] == '.' or s[i] == '?' or i == size - 1 or s[i] == '!':
            print("sentence has", words,"words")
            words = 1
        if s[i] == ' ' and s[i - 1] != '.' and s[i - 1] != '?' and s[i - 1] != '!' \
                and s[i + 1] != ' ' and s[i + 1] != '.' and s[i + 1] != '?' and s[i + 1] != '!':
            words += 1
            # print("so far was found", words,"words in currect sentences")

        if max < words:
            max = words
    return max

# test = "We test coders. Give us a try?"
# test = "Forget CVs..Save time . x x"
test = "?Is is a task!? Forget  CVs... This is a test case! Save time . x x"
print('max words is', solution(test))