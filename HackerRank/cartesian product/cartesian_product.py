from itertools import product
from itertools import product
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
result = list(product(a,b))
for i in result:
    print(i, end=' ')



#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'firstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING x
#

def firstOccurrence(s, x):
    # Write your code here
    if "*" in x :
        for i in range (len(x)):
            left,rigth = x.split("*")
        # print(left)
        # print(rigth)
        index_left = s.find(left)
        # print("f1",f1)
        if index_left!=-1:
            index_rigth = s[index_left:].find(rigth)
            # print("s[f1:]",s[f1:])
            # print("f2",f2)
            if index_rigth!=-1:
                return index_left
        else:
            return -1
    else:
        return s.find(x)
if __name__ == '__main__':