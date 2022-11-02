#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Task:
# The decimal zip of two non-negative integers A and B is an integer C whose
# decimal representation is created from the decimal representations of A and
# B as follows:
# - the  first digit of C is the first digit of A;
# - the second digit of C is the first  digit of B;
# - the  third digit of C is the second digit of A;
# - the fourth digit of C is the second digit of B;
# - etc
# If one of the integers A and B runs out of digits, the remaining digits of the
# other integer are appended to the result.
# The decimal representation of 0 is assumed to be "0".
# For example, the decimal zip of 12 and 56 is 1526.
# The decimal zip of 56 and 12 is 5162.
# The decimal zip of 12345 and 678 is 16273845.
# The decimal zip of 123 and 67890 is 16273890.
# The decimal zip of 1234 and 0 is 10234.
# Write a function that given two non-negative A and B, returns their decimal zip.
# The function should return -1 if the result exceeds 100,000,000.
# Assume that A and B are integers within the range [0..100,000,000].
# Focus on correctness not on performance

import random
def solution(a,b):
    astr= str(a)
    bstr =str(b)
    alen = len(str(a))
    blen=len(str(b))
    result = ""
    o=0
    if alen <= blen:
        alen = blen
    else:
        blen=alen
    for i in range(0,alen+1):
        result += str(astr[i:i+1])
        for j in range(o,blen+1):
            result += str(bstr[j:j+1])
            o += 1
            if int(result) > 100000000:
                return -1
            break
    return int(result)
n = 10
miny = -10
maxy = 10
w=[n]
# for p in range(n):
#     w.append(random.randint(miny,maxy))
# print(w)
# print('res=',solution(w))

# example 16273890
test1 = 123
test2 = 67890
# example 11 000 000
# test1 = 1000
# test2 = 1000
# example C=-1
# test1 = 13579
# test2 = 246800
print('A=', test1,'\nB=',test2)
print('C=', solution(test1,test2))