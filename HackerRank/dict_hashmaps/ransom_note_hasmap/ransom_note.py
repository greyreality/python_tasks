#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # print(magazine, note)
    result = "No"
    for i in note:
        if i in magazine:
            result = "Yes"
            ind = magazine.index(i)
            del magazine[ind]
        else:
            result = "No"
            break
    print(result)


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
