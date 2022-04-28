# Exercise on HackInScience:
# https://www.hackinscience.org/exercises/reverse-roman-numerals

# Tips & discussions (Solutions 2, 3, and 5 come from this link):
# https://stackoverflow.com/questions/19308177/converting-roman-numerals-to-integers-in-python

# Reverse Roman Numerals
# Created by Julien Palard
#
# Write a function named from_roman_numeral that return the value of a given roman numeral.
#
# Example
# >>> print(from_roman_numeral("V"))
# 5
# >>> print(from_roman_numeral("XX"))
# 20
# >>> print(from_roman_numeral("DCCC"))
# 800
# >>> print(from_roman_numeral("MMMM"))
# 4000

####################################################################################################################

# Solution 1 (a bit clumsy and technically INCORRECT) - this solution will pass the exercise, but won't work for 
# such Roman numerals as XIV (it will return 16 rather than 14).

def from_roman_numeral(roman_numeral):
    lookup = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
              'CM': 900, 'M': 1000}
    if roman_numeral in lookup.keys():
        return lookup.get(roman_numeral)
    else:
        temp = []
        for i in roman_numeral:
            j = lookup.get(i)
            temp.append(j)
        return sum(temp)
      
####################################################################################################################

# To fix this problem, it's crucial to understand the following:
# (https://stackoverflow.com/questions/19308177/converting-roman-numerals-to-integers-in-python/48557664#48557664)

# Roman numerals are read from left to right, as you add or subtract the value of each symbol.
# If a value is lower than the following value, it will be subtracted. Otherwise it will be added.

# For example, we want to conver the Roman numeral MCMLIV to an Arabic number:
#
# M = 1000 must be added, because the following letter C =100 is lower.
# C = 100 must be subtracted because the following letter M =1000 is greater.
# M = 1000 must be added, because the following letter L = 50 is lower.
# L = 50 must be added, because the following letter I =1 is lower.
# I = 1 must be subtracted, because the following letter V = 5 is greater.
# V = 5 must be added, because there are no more symbols left.

####################################################################################################################

# In other words:
# IV = V - I (4 = 5-1)
# IX = X - I (9 = 10-1)
# XL = L - X (40 = 50-10)
# XC = C - X (90 = 100-10)
# CD = D - C (400 = 500-100)
# CM = M - C (900 = 1000-100)

####################################################################################################################

# Solution 2 - using the built-in function "enumerate":

def from_roman_numeral(roman_numeral):
    
    lookup = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    for i, c in enumerate(roman_numeral):
        if (i + 1) == len(roman_numeral) or lookup[c] >= lookup[roman_numeral[i + 1]]:
            result += lookup[c]
        else:
            result -= lookup[c]
            
    return result

####################################################################################################################

# Solution 3 - similar to the last one, using *-1 rather than -=, and doesn't use 'enumerate':
    
def from_roman_numeral(s):

    lookup = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }    
    num = 0

    for i in range(len(s)):
        if i != len(s)-1 and lookup[s[i]] < lookup[s[i+1]]:
             num += lookup[s[i]]*-1 # it uses *-1 here, rather than -=
        else:
             num += lookup[s[i]]

    return num

####################################################################################################################

# Solution 4 - my version combining the last two; so far my favorite.

def from_roman_numeral(s):
    
    lookup = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    for i in range(len(s)):
        if i != len(s)-1 and lookup[s[i]] < lookup[s[i+1]]:
             result -= lookup[s[i]]
        else:
             result += lookup[s[i]]

    return result

####################################################################################################################

# Solution 5 - using "replace":

def from_roman_numeral(s):

     lookup = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }    
     num = 0

     s = s.replace("IV", "IIII").replace("IX", "VIIII")
     s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
     s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

     for x in s:
        num += lookup[x]

     return num

####################################################################################################################
  
# Beyond the exercise - the following code will convert numbers to Roman numerals (reverse of the exercise).
# It makes good use of "divmod", a built-in function that I wasn't aware of. I found the code here:
# https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php

# def to_roman_numeral(num):
#     lookup = [
#         (1000, 'M'),
#         (900, 'CM'),
#         (500, 'D'),
#         (400, 'CD'),
#         (100, 'C'),
#         (90, 'XC'),
#         (50, 'L'),
#         (40, 'XL'),
#         (10, 'X'),
#         (9, 'IX'),
#         (5, 'V'),
#         (4, 'IV'),
#         (1, 'I'),
#     ]
#     res = ""
#     for (n, roman) in lookup:
#         (d, num) = divmod(num, n) # "d" would be the quotient, and "num" will be overwritten by the remainder
#         res += roman * d
#     print(res)
#
# to_roman_numeral(int(input("Please enter an integer: ")))

####################################################################################################################
