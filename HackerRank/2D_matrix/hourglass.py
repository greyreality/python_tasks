#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    num_of_rows = len(arr)
    num_of_col = len(arr[0])
    # print(num_of_rows,"x",num_of_col)
    result = []
    for i in range(num_of_rows):
        for j in range(num_of_col):
            # print(arr[i][j], end = " ")
            if (i + 2) <= num_of_col - 1 and (j + 2) <= num_of_rows - 1:
                sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                    j + 1] + arr[i + 2][j + 2]
                # print("sum=",sum)
                result.append(sum)
        # print()
    return max(result)


if __name__ == '__main__':
    fptr = open('output.txt', 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
