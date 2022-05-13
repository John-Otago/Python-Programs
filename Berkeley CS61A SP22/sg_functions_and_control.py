###############################################################################
# Berkeley CS 61A: Structure and Interpretation of Computer Programs (SICP)
# Spring 2022

# Recent iterations of CS61A (2011+) mostly use Python, vis-à-vis the original
# SICP that relies on Scheme. See https://teachyourselfcs.com/#programming

###############################################################################

# Study Guide: Functions and Control 

from doctest import run_docstring_examples

###############################################################################

# Q11: Last square
#
# Implement the function last_square, which takes as input a positive integer
# and returns the largest perfect square less than its argument. A perfect
# square is any integer multiplied by itself:
#
# Hint: If you're stuck, try writing a function that prints out the first 5
# perfect squares using a while statement: 1, 4, 9, 16, 25. Then, adapt that
# while statement to this question by changing the header.


def last_square(x):
    """Return the largest perfect square less than X, where X>0.

    >>> last_square(10)
    9
    >>> last_square(39)
    36
    >>> last_square(100)
    81
    >>> result = last_square(2) # Return, don't print
    >>> result
    1


    >>> cases = [(1, 0), (2, 1), (3, 1), (4, 1), (5, 4), (6, 4),
    ...          (10, 9), (17, 16), (26, 25), (36, 25), (46, 36)]
    >>> [last_square(s) == t for s, t in cases].count(False) # This is nice
    0

    """

    # Official solution:
    k = 0
    while k * k < x:
        k = k + 1
    return (k-1) * (k-1)


# Test the function
run_docstring_examples(last_square, globals(), True)
