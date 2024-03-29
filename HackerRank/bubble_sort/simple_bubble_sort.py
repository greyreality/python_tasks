#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countSwaps function below.
def countSwaps(n, a):
    s = 0
    for i in range(n):
        for j in range(n - 1):
            # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                s += 1
                # print(s)
    print("Array is sorted in", s, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[n - 1])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(n, a)
