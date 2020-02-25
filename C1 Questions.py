# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:34:08 2020

@author: Owner
"""
import re
from typing import List, TypeVar, Tuple, Any, Generator
from random import randrange, randint
Num = TypeVar('Num', int, float)

#Write a short Python function, is multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.
def is_multiple(n: int, m: int) -> bool:
    return True if n % m == 0 else False
is_multiple(4, 2), is_multiple(4, 3)

#Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.
def is_even(k: int) -> bool:
    return False if k & 1 else True
is_even(3), is_even(4)
#Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.
# Num = TypeVar('Num', int, float)
def minmax(data: List[Num]) -> Tuple[Num, Num]:
    min_num = max_num = data[0]
    for num in data:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num
minmax([1, 2, 3, 4])
#1.4: Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.
def sum_sq(n: int) -> int:
    return sum(i*i for i in range(1, n))

#1.5: Give a single command that computes the sum from Exercise R-1.4, rely- ing on Python’s comprehension syntax and the built-in sum function.
sum_sq(4)
#R-1.6: Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.
def sum_odd_sq(n: int) -> int:
    return sum(i*i for i in range(1, n) if not is_even(i))
#R-1.7: Give a single command that computes the sum from Exercise R-1.6, rely- ing on Python’s comprehension syntax and the built-in sum function.
sum_odd_sq(4)
#-1.8 Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for in- dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?
# j = n + k <=> k = j - n
def check(data: str='hello') -> bool:
    n = len(data)
    for j in range(n):
        k = j - n
        if data[j] != data[k]:
            return False
    return True

check()
#1.9 What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?
print(list(range(50, 90, 10)))
#1.10 What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
print(list(range(8, -10, -2)))
#1.11 Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
print([2**i for i in range(9)])
#1.12 Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module in- cludes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function.
def choice(data: List[Any]) -> Any:
    return data[randrange(0, len(data))]
def choice(data: List[Any]) -> Any:
    return data[randrange(0, len(data))]
#1.13 Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.
def reverse(data: List[Any]) -> List[Any]:
    n = len(data)
    return [data[i] for i in range(n-1, -1, -1)]
reverse([1, 2, 3, 4])
#1.14 Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.
def odd_pair(data: List[int]) -> bool:
    odd_nums = {num for num in data if not is_even(num)}
    return True if len(odd_nums)>=2 else False
odd_pair([2, 3, 3, 4]), odd_pair([2, 3, 3, 5])
#C 1.15 Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).
def is_unique(data: List[Num]) -> bool:
    return len(data) == len(set(data)) 




