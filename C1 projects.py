# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:26:15 2020

@author: Owner
"""

#P-1.29 Write a Python program that outputs all possible strings formed by using the characters c , a , t , d , o , and g exactly once.
def add_char(char: str, string_list: List[str]) -> List[str]:
    return [char + string for string in string_list]

def flatten_lists(lists:List[List[Any]]) -> List[Any]:
    result = []
    for l1 in lists:
        result += l1
    return result

def permutation(chars: str) -> List[str]:
# Base case
    if len(chars) == 1:
        return [chars]
    return flatten_lists([add_char(chars[i], permutation(chars[:i] + chars[i+1: ])) 
                            for i in range(len(chars))])
# 3! = 3 * 2 * 1 = 6
permutation('abc')
#P-1.30 Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.
def my_log(n: int) -> int:
    if n < 2:
        return 0
    elif n < 4:
        return 1
    return 1 + my_log(n / 2)
my_log(8), my_log(7.5)

