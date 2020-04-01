# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:20:33 2020

@author: WEIMIN ZHOU
"""

def get_digit_sum(a):
    if a <= 0:
        return 0
    res = 0
    while a > 0:
        res += a%10
        a //= 10
    return res

def maxSum(A):
    max_sum = -float('inf')
    dic = {}
    for a in A:
        digit_sum = get_digit_sum(a)
        if digit_sum not in dic:
            dic[digit_sum] = a
        else:
            max_sum = max(max_sum, dic[digit_sum]+a)
            dic[digit_sum] = max(dic[digit_sum], a)
    return max_sum if max_sum != -float('inf') else -1

print(maxSum([51, 71, 17, 42]))

