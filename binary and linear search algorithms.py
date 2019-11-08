# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:00:30 2019

@author: Owner
"""
#remember in this version of Python print is a function!
#linear search
def linear_search(A, x):
  for element in A:
    if element == x:
      return 'x is found'
  return 'x is not found'
A = [3, 5, 11, 6, 9, 23, 12, 13, 4]
x = 12
print ("linear search(A, k)")

# iterative binary search
def binarySearch(arr, l, x, y): 
    while l <= x: 
        mid = l + (x - l)/2;
        # Check if y is present at mid 
        if arr[mid] == y: 
            return mid 
        If y is greater, ignore left half 
        elif arr[mid] < y: 
            l = mid + 1
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
    # If we reach here, then the element was not present 
    return -1
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index %d" % result 
else: 
    print "Element is not present in array"

#recursive binary search
    # Returns index of x in arr if present, else -1 
def binarySearch (arr, l, x, y): 
  
    # Check base case 
    if x >= l: 
  
        mid = l + (x - l)/2
  
        # If element is present at the middle itself 
        if arr[mid] == y: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > y: 
            return binarySearch(arr, l, mid-1, y) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarySearch(arr, mid+1, x, y) 
  
    else: 
        # Element is not present in the array 
        return -1
    # Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index %d" % result 
else: 
    print "Element is not present in array"



        

