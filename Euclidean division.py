# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:05:40 2020

@author: Owner
"""

print(10%3)
def computeGCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 
x = 6209
y = 4435
print(computeGCD(6209, 4435))
print(18 < -4)
print (18 >= -4)
print(18 != -4)


