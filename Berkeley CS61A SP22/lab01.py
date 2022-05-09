###############################################################################
# Berkeley CS 61A: Structure and Interpretation of Computer Programs (SICP)
# Spring 2022

# Recent iterations of CS61A (2011+) mostly use Python, vis-à-vis the original
# SICP that relies on Scheme. See https://teachyourselfcs.com/#programming

###############################################################################

# Lab 01: I'm skipping WWPD (What Would Python Do/Display)

from doctest import run_docstring_examples

###############################################################################

# Q4: Add in Range
#
# Complete add_in_range, which returns the sum of all integers between start
# and stop (inclusive).

def add_in_range(start, stop):
    """
    >>> add_in_range(3, 5)  # .Case 1
    12
    >>> add_in_range(1, 10)  # .Case 2
    55

    # I've added a few additional tests
    >>> add_in_range(0, 4)  # .Case 3
    10
    >>> add_in_range(125, 126)  # .Case 4
    251
    >>> add_in_range(-10, -9)  # .Case 5
    -19
    """

    # My solution:
    return sum(range(start, stop+1))

    # Official solution:
    total = 0
    while start <= stop:
        total += start
        start += 1
    return total

# Test the function
run_docstring_examples(add_in_range, globals(), True)

###############################################################################


# Q5: Digit Position Match
#
# A number has a digit-position match if the ith-to-last digit is i. For
# example,980 has the 0th-to-last digit as 0. Or 98276 has the 2nd-to-last
# digit as a 2.
#
# Write a function that determine if a number n has a digit-position match at a
# kth-to-last digit k.

def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    
    # My solution:
    if not str(k) in str(n):
        return False
    elif k == str(n)[::-1].index(str(k)):
        return True
    else:
        return False
    
    # Official solution:
    index = 0
    while index < k:
        n = n // 10
        index = index + 1
    return n % 10 == k
        
# Test the function
run_docstring_examples(digit_pos_match, globals(), True)

###############################################################################
