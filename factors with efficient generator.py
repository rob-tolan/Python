# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:19:31 2020

@author: Owner
"""
def factors(n):
    k =1
while k*k<n:
    if n%k == 0:
    yield k
yield n//k
k += 1 
if k*k == n:
    yield k
    