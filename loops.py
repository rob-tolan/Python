# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:55:00 2020

@author: Owner
"""
#checking if prime
num = 5
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "is not prime")
            break
    else:
     print(num, "is prime")
else:
    print(num, "is not prime")
    