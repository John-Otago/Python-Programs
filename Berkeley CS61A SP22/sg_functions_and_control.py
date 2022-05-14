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

# Discussion:
# I like how they tested multiple cases using a single list (lines 41-44)
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

# Q13: Triangular numbers
#
# The nth triangular number is defined as the sum of all integers from 1 to n,
# i.e.
#
# 1 + 2 + ... + n
#
# The closed-form formula for the nth triangular number is
#
# (n + 1) * n / 2
#
# Define triangular_sum, which takes an integer n and returns the sum of the
# first n triangular numbers, while printing each of the triangular numbers
# between 1 and the nth triangular number.


def triangular_sum(n):
    """
    >>> t_sum = triangular_sum(5)
    1
    3
    6
    10
    15
    >>> t_sum
    35
    """

    # My solution:
    mylist = []
    for i in range(1, n+1):
        print(int((i + 1) * i / 2))
        mylist.append(int((i + 1) * i / 2))
    return sum(mylist)

    # Official solution:
    count = 1
    t_sum = 0
    while count <= n:
        t_number = count * (count + 1) // 2
        print(t_number)
        t_sum += t_number
        count += 1
    return t_sum


# Test the function
run_docstring_examples(triangular_sum, globals(), True)
###############################################################################

# Q14: Same hailstone
#
# Implement same_hailstone, which returns whether positive integer arguments a
# and b are part of the same hailstone sequence. A hailstone sequence is
# defined in Homework 1 as the following:
#
#     Pick a positive integer n as the start.
#     If n is even, divide it by 2.
#     If n is odd, multiply it by 3 and add 1.
#     Continue this process until n is 1.


def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """

# Collatz conjecture (hailstone sequence):
# https://en.wikipedia.org/wiki/Collatz_conjecture

# Hailstone sequence generator:
# https://www.dcode.fr/collatz-conjecture


# My (super clumsy) solution:
    list_a = [a]
    list_b = [b]
    a_original = a
    b_original = b
    while a > 1:
        if a % 2 == 0:
            list_a.append(a/2)
            a = a/2
        elif a % 2 != 0:
            list_a.append(a*3+1)
            a = a*3+1
    while b > 1:
        if b % 2 == 0:
            list_b.append(b/2)
            b = b/2
        elif b % 2 != 0:
            list_b.append(b*3+1)
            b = b*3+1
    if len(list_a) >= len(list_b):
        return a_original in list_a and b_original in list_a
    else:
        return a_original in list_b and b_original in list_b

# Official solution:
# (It's not necessary to return the whole hailstone sequence!)

    return in_hailstone(a, b) or in_hailstone(b, a)

def in_hailstone(a, b):
    """Return whether b is in hailstone sequence of a."""
    while a > 1:
        if a == b:
            return True
        elif a % 2 == 0:
            a = a // 2
        else:
            a = a * 3 + 1
    return False


# Test the function
run_docstring_examples(same_hailstone, globals(), True)
###############################################################################
