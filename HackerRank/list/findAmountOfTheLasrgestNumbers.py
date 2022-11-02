#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    candles_set = set(candles)
    max_in_set = max(candles_set)
    amount = 0
    # print(candles_set)
    # print(max_in_set)
    # print(amount)

    for x in candles:
        if x == max_in_set:
            amount += 1

    return amount

if __name__ == '__main__':
    candle_list = [3, 2, 1, 3]
    print(birthdayCakeCandles(candle_list))