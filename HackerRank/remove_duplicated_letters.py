#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def remove_duplicated_letters(str1):
    result = []
    for i in str1:
        if i not in result:
            result.append(i)
        # print(i)
    makeitastring = ''.join(map(str, result))
    return makeitastring

str1 = "hellohi"
str2 = "thisisarandomsentance"
print(remove_duplicated_letters(str1))
print(remove_duplicated_letters(str2))