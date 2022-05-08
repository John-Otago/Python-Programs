###############################################################################
# Berkeley CS 61A: Structure and Interpretation of Computer Programs (SICP)
# Spring 2022

# Recent iterations of CS61A (2011+) mostly use Python, vis-à-vis the original
# SICP that relies on Scheme. See https://teachyourselfcs.com/#programming
###############################################################################

# Homework 01

from doctest import run_docstring_examples

###############################################################################

# Q2: k in Num

def k_in_num(k, num):
    """
    Complete k_in_num, a function which returns True if num has the digit k and
    returns False if num does not have the digit k. 0 is considered to have no
    digits.

    >>> k_in_num(3, 123) # .Case 1
    True
    >>> k_in_num(2, 123) # .Case 2
    True
    >>> k_in_num(5, 123) # .Case 3
    False
    >>> k_in_num(0, 0) # .Case 4
    False
    """

# My solution
    if k != 0 and num != 0:
        return str(k) in str(num)
    else:
        return False

# Official solution
    while num:
        if k == num % 10:
            return True
        num = num // 10
    return False

# Test the function
run_docstring_examples(k_in_num, globals(), True)

# Comments
# My rationale is that integers are not iterable, and hence it's easier to 
# turn both k and num into strings (not sure if it's cheating or an acceptable 
# shortcut?).
# 
# The official solution also makes a lot of sense.

###############################################################################
