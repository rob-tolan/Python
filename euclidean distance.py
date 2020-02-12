# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 01:54:08 2020

@author: Owner
"""

import math
#function to calculate distance
def distance(x1, y1, x2, y2):
    #calculating distance
    return math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2)*1)