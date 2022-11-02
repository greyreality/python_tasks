#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# run time error
import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(n,a, d):
    b = [None] * n
    for i in range(n):
        print("current index=",i, "value=",a[i])
        if i-d<0:
            b[n-abs(i-d)] = a[i]
            print("future index=",n-abs(i-d), "b=",b)
        else:
            b[i-d] = a[i]
            print("future index=",i-d, "b=",b)
    return b

if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(n,a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
