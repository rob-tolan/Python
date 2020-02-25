# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:07:53 2020

@author: Owner
"""

class vector:
#represent a vector in multidimensional space.
    
def _init_(self, d):

#create d-dimensional vector of zeros.
self.cords = [0]*d
def _len(self):
#return dimension of vector.
return len(self._coords)

def _getitem_(self,j):
#return hth coordinate of vector.
return self._coords[j]
def _ _ setitem_(self,j,val):
#set jth coordinate to given value
self._coords[j]=val
def _add_(self, other):
#return sum of the vectors
if len(self) != len(other):
#relies on _len_method

raise ValueError('dimensions must agree')
result = vector(len(self)) start with vector of zeros
for j in range(len(self)):
    result[j]=self[j]+other[j]
    return result
def _eq_(self,other):
    return self._coords==other._coords
def _ _ ne_(self,other):
"""Return True if vector differs from other """
return not self ==other. rely on existing_eq_definition

def _str_(self):
    
"""Produce string representation of vector """
return '<' +str(self_coords)[1:-1] + '>' adapt list representation.