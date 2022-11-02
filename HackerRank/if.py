#!/bin/python3

import math
import os
import random
import re
import sys


def main(n):
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
    # print(type(n))
    # if (n % 2 != 0):
    #     print("Weird")
    # if n <= 2 and n >= 5:
    #     print("Not Weird")
    # if n <= 6 and n >= 20:
    #     print("Weird")
    # if n > 20:
    #     print("Not Weird")
    # print(n)

if __name__ == '__main__':
    n = int(input().strip())
    main(n)
