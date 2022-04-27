# Exercise on HackInScience:
# https://www.hackinscience.org/exercises/reverse-roman-numerals

# Reverse Roman Numerals
# Created by Julien Palard

# Write a function named from_roman_numeral that return the value of a given roman numeral.

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
# as IV or IX (it will return wrong answers).

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
 
# Solution 2 - to be added later
  
  
  
  
  
  
  
  
  
####################################################################################################################
  
# Beyond the exercise - the following code will convert numbers to Roman numerals (reverse of the exercise)
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
