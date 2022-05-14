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

###############################################################################

# Q12: Overlaps
#
# An open interval is a range of numbers that does not include its end points.
# For example, (10, 15) stands for all numbers that are strictly greater than
# 10 and strictly less than 15. Two intervals overlap if they contain any
# points in common. For example (10, 15) overlaps (14, 16), but not (1, 5) or
# (15, 16). The intervals (10, 10) or (10, 9) contain no numbers, since nothing
# is both greater than and less than 10, or greater than 10 and less than 9.
# Implement the function overlaps to take four numbers as arguments,
# representing the bounds of two intervals, and return True if the intervals
# overlap and False otherwise.


def overlaps(low0, high0, low1, high1):
    """Return whether the open intervals (LOW0, HIGH0) and (LOW1, HIGH1)
    overlap.

    >>> overlaps(10, 15, 14, 16)
    True
    >>> overlaps(10, 15, 1, 5)
    False
    >>> overlaps(10, 10, 9, 11)
    False
    >>> result = overlaps(1, 5, 0, 3)  # Return, don't print
    >>> result
    True


    >>> [overlaps(a0, b0, a1, b1) for a0, b0, a1, b1 in
    ...       ( (1, 4, 2, 3), (1, 4, 0, 2), (1, 4, 3, 5), (0.1, 0.4, 0.2, 0.3),
    ...         (2, 3, 1, 4), (0, 2, 1, 4), (3, 5, 1, 4) )].count(False)
    0
    >>> [overlaps(a0, b0, a1, b1) for a0, b0, a1, b1 in
    ...       ( (1, 4, -1, 0), (1, 4, 5, 6), (1, 4, 4, 5), (1, 4, 0, 1),
    ...         (-1, 0, 1, 4), (5, 6, 1, 4), (4, 5, 1, 4), (0, 1, 1, 4),
    ...         (5, 5, 3, 6), (5, 3, 4, 6), (5, 5, 5, 5),
    ...         (3, 6, 5, 5), (4, 6, 5, 3), (0.3, 0.6, 0.5, 0.5) )].count(True)
    0
    """

    # Official solution:
    return low1 < min(high0, high1) > low0


# Test the function
run_docstring_examples(overlaps, globals(), True)

###############################################################################
