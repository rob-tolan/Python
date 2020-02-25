# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:20:15 2020

@author: Owner
"""
def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k 