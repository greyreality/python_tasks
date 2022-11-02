#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    # print(arr)
    max_sum = float(0)
    min_sum = float(0)
    for i in range(len(arr)):
        # print(i, arr[i])
        if i != 4:
            min_sum = min_sum + arr[i]
        if i != 0:
            max_sum = max_sum + arr[i]
    print("{0:0.0f}".format(min_sum), "{0:0.0f}".format(max_sum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
