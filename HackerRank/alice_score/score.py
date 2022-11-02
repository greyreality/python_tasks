#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rev_alice,short_score, rev_place = [], [], []
    for i in scores:
        if i not in short_score:
            short_score.append(i)
    for i in reversed(alice):
        # if i not in rev_alice:
        rev_alice.append(i)
    print("peoples_score:",short_score)
    print("alice_score:",rev_alice)
    place = []
    for j in range(len(rev_alice)):
        for i in range(len(short_score)):
            # print("alice_score=",rev_alice[j], "score=", short_score[i])
            if rev_alice[j] == short_score[i]:
                place.append(i + 1)
                break
            elif rev_alice[j] > short_score[i]:
                place.append(i+1)
                break
            elif (rev_alice[j] < short_score[i]) and (i == len(short_score)-1):
                place.append(i+2)
                break
    for i in reversed(place):
        rev_place.append(i)
    return rev_place

if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# input
# 6
# 100 90 90 80 75 60
# 5
# 50 65 77 90 102