#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'whatFlavors' function below.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money

def whatFlavors(cost, money):
    print("money=", money)
    # print("len=", len(cost))
    print("cost=", cost)

    # o = list(enumerate(cost))
    # print(o)
    saved = {}    #create a dict

    # for index and value in cost[i]=n
    for index, n in enumerate(cost):
        print("index=", index, "number=", n)
        print("diff=", money - n)
        if money - n in saved:
            print("yeah")
            return saved[money - n], index + 1
        print("no")
        saved[n] = index + 1
        print(saved)

if __name__ == '__main__':
    # t = int(input().strip())
    t = 2
    money = 4
    n = 5
    cost = (5,4,1,3,2)
    l = whatFlavors(cost, money)
    print("money=", money)
    print("answer indexes=", l[0], l[1])
    print("cost=", cost)

    # for t_itr in range(t):
        # money = int(input().strip())

        # n = int(input().strip())

        # cost = list(map(int, input().rstrip().split()))

        # l = whatFlavors(cost, money)
        # print(l[0], l[1])

# Input (stdin)
#
# Download
# 2
# 4
# 5
# 1 4 5 3 2
# 4
# 4
# 2 2 4 3
# Your Output (stdout)
# 1 4
# 1 2

# ===================== The Brute-force solution:

# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'whatFlavors' function below.
# #
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY cost
# #  2. INTEGER money
# #
#
# def whatFlavors(cost, money):
#     # print(money)
#     # print("len=", len(cost))
#     # print(cost)
#     # print(cost)
#
#     i = 0
#     result = False
#     while i < len(cost) - 1:
#         # print("i=",i)
#         if cost[i] < money:
#             diff = money - cost[i]
#             for j in range(len(cost) - 1):
#                 if (i != j) & (diff == cost[j]) & (j > i):
#                     print(str(i + 1) + " " + str(j + 1))
#                     break
#                 elif (i != j) & (diff == cost[j]) & (j > i):
#                     print(str(j + 1) + " " + str(i + 1))
#                     break
#         i += 1
#
#
# if __name__ == '__main__':
#     t = int(input().strip())
#
#     for t_itr in range(t):
#         money = int(input().strip())
#
#         n = int(input().strip())
#
#         cost = list(map(int, input().rstrip().split()))
#
#         whatFlavors(cost, money)
# Input (stdin)
#
# Download
# 2
# 4
# 5
# 1 4 5 3 2
# 4
# 4
# 2 2 4 3
# Your Output (stdout)
# 1 4
# 1 2