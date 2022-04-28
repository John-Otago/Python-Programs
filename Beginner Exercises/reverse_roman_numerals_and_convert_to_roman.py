# Exercise on HackInScience:
# https://www.hackinscience.org/exercises/reverse-roman-numerals

# Tips & discussions:
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

# Solution 1 (technically INCORRECT) - this solution will pass the exercise, but won't work for such Roman numerals
# as XIV (it will return 16 rather than 14).

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

# Solution 3 - similar to the last one, but simpler and doesn't use 'enumerate'
    
def from_roman_numeral(s):

    lookup = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }    
    num = 0

    for i in range(len(s)):
        if i != len(s)-1 and lookup[s[i]] < lookup[s[i+1]]:
             num += lookup[s[i]]*-1
        else:
             num += lookup[s[i]]

    return num

####################################################################################################################

# Solution 4 - using "replace":

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
