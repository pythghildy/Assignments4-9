# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:58:49 2019

@author: rahulgh
"""

# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False