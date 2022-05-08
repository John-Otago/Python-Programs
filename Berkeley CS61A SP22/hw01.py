###############################################################################
# Berkeley CS 61A: Structure and Interpretation of Computer Programs (SICP)
# Spring 2022

# Recent iterations of CS61A (2011+) mostly use Python, vis-à-vis the original
# SICP that relies on Scheme. See https://teachyourselfcs.com/#programming
###############################################################################

# Homework 01
# You should try your own solutions before checking my version below.

from doctest import run_docstring_examples

###############################################################################

# Q2: k in Num
# Write a function k_in_num which takes in two integers, k and num. k_in_num 
# returns True if num has the digit k and returns False if num does not have 
# the digit k. 0 is considered to have no digits.

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

# Q3: A Plus Abs B
# Python's operator module defines binary functions for Python's intrinsic
# arithmetic operators. For example, calling operator.add(2,3) is equivalent
# to calling the expression 2 + 3; both will return 5.
#
# Fill in the blanks in the following function for adding a to the absolute
# value of b, without calling abs. You may not modify any of the provided code
# other than the two blanks.

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """

    # My solution:
    if b < 0:
        return a - b
    else:
        return a + b

    # Official solution:
    from operator import add, sub
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b) 
    # This is elegant--a good demo of abstraction, defined as 'general patterns
    # of flow controls' in the original Scheme-based SICP. I never thought we 
    # could use functions like this until CS61A/SICP.

# Test
run_docstring_examples(a_plus_abs_b, globals(), True)

###############################################################################

# Q4: Two of Three
#
# Write a function that takes three positive numbers as arguments and returns
# the sum of the squares of the two smallest numbers. Use only a single line
# for the body of the function.

def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """

    # My solution: same as the official alternative solution below

    # Official solution:
    return min(i * i + j * j, i * i + k * k, j * j + k * k)

    # Official alternative solution
    return i ** 2 + j ** 2 + k ** 2 - max(i, j, k) ** 2

# Test
run_docstring_examples(two_of_three, globals(), True)

###############################################################################

# Q5: Largest Factor
# Write a function that takes an integer n that is greater than 1 and returns
# the largest integer that is smaller than n and evenly divides n.

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1

    # I have added a few tests to run:
    >>> largest_factor(22) # factor is 1, 2, 11
    11
    >>> largest_factor(26) # factor is 1, 2, 13
    13
    >>> largest_factor(60) # factor is 1, 2, 3, 5, 6, 10, 12, 20, 30
    30
    >>> largest_factor(77) # factor is 1, 7, 11
    11
    """

    # My initial solution:
    num_list = []
    for i in range(1, n):
        if n % i == 0:
            num_list.append(i)
    return max(num_list)

    # Official solution:
    factor = n - 1
    while factor > 0:
        if n % factor == 0:
            return factor
        factor -= 1

    # My final (improved) solution
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

run_docstring_examples(largest_factor, globals(), True)

###############################################################################
