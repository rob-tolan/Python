# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:29:48 2020

@author: Owner
"""

name_function = lambda arguments : result
def square(x):
  return x**2
square_2 = lambda x: x**2
print(square_2(4))
#working with production functions
def production(l, k, m):
  """
  Returns the value of the production according to
  labour, capital and materials

  Keyword arguments:
  l -- labour (float)
  k -- capital (float)
  m -- materials (float)
  """
  return l**0.3 * k**0.5 * m**(0.2)
production_2 = lambda l,k,m : l**0.3 * k**0.5 * m**(0.2)
print(production(42, 40, 42))
print(production_2(42, 40, 42))

import statistics
def desc_stats(x):
  """Returns the mean and standard deviation of `x`"""
  return {"mean": statistics.mean(x),
  "std_dev": statistics.stdev(x)}

x = [1,3,2,6,4,1,8,9,3,2]
res = desc_stats(x)
print(res)


