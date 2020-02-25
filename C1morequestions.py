# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:12:59 2020

@author: Owner
"""

#C 1.18  Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
print([n * (n+1) for n in range(0, 10)])
#C1.19 Demonstrate how to use Python’s list comprehension syntax to produce the list [ a , b , c , ..., z ], but without having to type all 26 such characters literally
print([chr(ord('a')+i) for i in range(0, 26)])
#C-1.20 Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each possi- ble order occurs with equal probability. The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using only the randint function, implement your own version of the shuffle function.
def shuffle(data: List[Any]) -> None:
    n = len(data)
    for i in range(n-1, 0, -1):
        j = randint(0, i-1)
        data[i], data[j] = data[j], data[i]
l1 = [1, 2, 3, 4]
shuffle(l1)
l1
#C 1.21 Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, and then outputs those lines in reverse order (a user can indicate end of input by typing ctrl-D).
def print_reverse() -> None:
    lines = []
    while 1:
        try:
            line = input("input something: ")
        except EOFError:
            break
        lines.append(line)
    print("\n")
    for line in reversed(lines):
        print(line)
#C-1.22 Write a short Python program that takes two arrays a and b of length n storing int values, and returns the dot product of a and b. That is, it returns an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.
def array_product(a: List[int], b: List[int]) -> List[int]:
    return [i * j for i, j in zip(a, b)]
array_product([1, 3, 5], [2, 4, 6])
#1.23 Give an example of a Python code fragment that attempts to write an ele- ment to a list based on an index that may be out of bounds. If that index is out of bounds, the program should catch the exception that results, and print the following error message: “Don’t try buffer overflow attacks in Python!”
def check_overflow() -> None:
    data = [1, 2, 3]
    try:
        data[3] = 0
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")
check_overflow()
#C-1.24 Write a short Python function that counts the number of vowels in a given character string.
def get_vowels(data: str) -> int:
    vowels = 'aeiou'
    #vowels = ['a', 'e', 'i', 'o', 'u']
    return len([i for i in data.lower() if i in vowels])
get_vowels('hello')
#C-1.25 Write a short Python function that takes a string s, representing a sentence, and returns a copy of the string with all punctuation removed. For exam- ple, if given the string "Let s try, Mike.", this function would return "Lets try Mike".
def remove_punctuation(sentence: str) -> str:
    removed = [char for char in sentence 
                if (ord('A') <= ord(char) <= ord('z')) or ord(char) == ord(' ')]
    return ''.join(removed)
remove_punctuation("Let's try, Mike.")
#C-1.26 Write a short program that takes as input three integers, a, b, and c, from the console and determines if they can be used in a correct arithmetic formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”
def check_op_right() -> bool:
    nums = input("input int a, b, c: ")
    operators = '+-*/'

    # case1: a = b op c
    a, b_c_str = re.findall(r'(\d+), (\d+, \d+)', nums)[0]
    case1 = [int(a) == eval(b_c_str.replace(', ', op)) for op in operators]
    result = sum(case1)
    
    # case2: a op b = c
    a_b_str, c = re.findall(r'(\d+, \d+), (\d+)', nums)[0]
    case2 = [int(c) == eval(a_b_str.replace(', ', op)) for op in operators]
    result += sum(case2)

    return result > 0
check_op_right(), check_op_right()
#C-1.27 In Section 1.8, we provided three different implementations of a generator that computes factors of a given integer. The third of those implementa- tions, from page 41, was the most efficient, but we noted that it did not yield the factors in increasing order. Modify the generator so that it reports factors in increasing order, while maintaining its general performance ad- vantages.
def factors(n: int) -> Generator[int, None, None]:
    k = 1
    larger_factors = []
    while k*k < n:
        if n % k == 0:
            yield k
            larger_factors.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for num in reversed(larger_factors):
        yield num
list(factors(100))
#C-1.28  The p-norm of a vector v = (v 1 , v 2 , . . . , v n ) in n-dimensional space is de- fined as:
#∥v∥=vp1+vp2+⋯+vpn−−−−−−−−−−−−−−√p
#For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the vector. Give an implemen- tation of a function named norm such that norm(v, p) returns the p-norm value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.
def norm(v: List[Num], p: int=2) -> Num:
    return sum(i**p for i in v) ** (1/p)
norm([4, 3])
