#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Task:
# Your monthly phone bill has just arrived, and it's unexpectedly large. You
# decide to verify the amount by recalculating the bill based on your phone call
# logs and the phone company's charges.
# The logs are given as a string S consisting of N lines separated by end-of-line
# characters (ASCII code 10). Each line describes one phone call using the
# following format: "hh:mm:ss, nnn-nnn-nnn", where "hh:mm:ss" denotes the
# duration of the call (in hours, munites, seconds) and
# "nnn-nnn-nnn" denotes the 9-digit phone number of the recipient
# (with no leading zeros).
# Each call is billed separately. The billing rules are as follows:
# - if the call was shorter than 5 minutes, then you pay 3 cents for
# every started second of the call (e.g. for duration "00:01:07" you pay
# 67*3=201 cents).
# - if the call was at least 5 minutes long, then you pay 150 cents
# for every started munite of the call
# (e.g. for duration "00:05:00" you pay 5*150=750 cents and
# for duration "00:05:01" you pat 6*150 = 900 cents).
# - All calls to the phone number that has the longest total
# duration of calls are free. In the case of a tie, if more than one
# phone number shares the longest total duration, the promotion
# is applied only to the phone number whose numerical value is
# the smallest among these phone numbers.
#
# Write a function that, given a string S describing phone call logs, returns the
# amount of money you have to pay in cents.
# For example: "00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090"
# the function should return 900
# (the total duration for number 400-234-090 is 6min 7sec,
#  total for 701-080-080 is 5min 1 sec, therefore, the free promotion applies to
# the former phone number)
# Focus on correctness not on performance

import operator
def tariff(h, m, s):
    all = s + m * 60 + h * 60 * 60
    if all < 5 * 60:
        return 3 * all
    else:
        if s != 0:
            return (m + 1) * 150
        else:
            return m * 150
def solution(s):
    # print(s)
    lines = s.splitlines()
    # print(lines)
    hours, minutes, secs = 0, 0, 0
    num = {}
    for i in lines:
        # print(i)
        hours = int(i[0:2])
        minutes = int(i[3:5])
        secs = int(i[6:8])
        number = str(i[9:20])
        if str(number) in num:
            # print('before=', num[number])
            temp = num[number] + tariff(hours, minutes, secs)
            num[number] = temp
            # print('after=',num[number])
        else:
            num[number] = tariff(hours, minutes, secs)
        # print(num)
        # print(number)
    print('phones debts=', num)
    # print('max val=',max(num.items(), key=operator.itemgetter(1))[0])
    del num[max(num.items(), key=operator.itemgetter(1))[0]]
    print('final=', num)
    return sum(num.values())

# test = '00:01:07,400-234-090\n' \
#        '00:05:01,701-080-080\n' \
#        '00:05:00,400-234-090'

test = '00:01:07,400-234-090\n' \
       '00:01:07,301-080-080\n' \
       '00:05:00,400-234-090\n' \
       '00:05:00,301-080-080'
print('to pay in cents=', solution(test))