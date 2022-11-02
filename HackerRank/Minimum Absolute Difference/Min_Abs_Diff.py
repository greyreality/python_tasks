#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    l = len(arr)
    diff = 0
    d = set()
    arr = sorted(arr)
    print("sort arr=", arr)
    for i in range(l - 1):
        for j in range(i + 1, l):
            print("i=", i, "j=", j)
            diff = abs(arr[i] - arr[j])
            d.add(diff)
            print(diff)

    return min(d)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
