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

# Q6: Falling Factorial
#
# Let's write a function falling, which is a "falling" factorial that takes two
# arguments, n and k, and returns the product of k consecutive numbers,
# starting from n and working downwards. When k is 0, the function should
# return 1.


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """

    # My solution (recursion):
    if k == 0:
        return 1
    else:
        return n * falling(n-1, k-1)
    
    # Official solution (iteration + new variables "total" and "stop"):
    total, stop = 1, n-k
    while n > stop:
        total, n = total*n, n-1
    return total
    

# Test the function
run_docstring_examples(falling, globals(), True)

###############################################################################

# Q7: Sum Digits
#
# Write a function that takes in a nonnegative integer and sums its digits.
# (Using floor division and modulo might be helpful here!)


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you use return rather than print
    >>> a
    6
    """

    # My solution:
    total, mylist = 0, [int(x) for x in str(y)]
    while mylist:
        total += mylist.pop()
    return total

    # Official solution:
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total


# Test the function
run_docstring_examples(sum_digits, globals(), True)

###############################################################################

# Q9: K-Occurrence
#
# Complete k_occurrence, a function which returns the number of times the digit
# k appears in num. 0 is considered to have no digits.


def k_occurrence(k, num):
    """
    >>> k_occurrence(5, 10)  # .Case 1
    0
    >>> k_occurrence(5, 5115)  # .Case 2
    2
    >>> k_occurrence(0, 100)  # .Case 3
    2
    >>> k_occurrence(0, 0)  # .Case 4
    0
    """

    # My solution
    if num == 0:
        return 0
    else:
        return str(num).count(str(k))

    # Official solution:
    occurrences = 0
    while num:
        if num % 10 == k:
            occurrences += 1
        num = num // 10
    return occurrences


# Test the function
run_docstring_examples(k_occurrence, globals(), True)

###############################################################################

# Q10: Double Eights
#
# Write a function that takes in a number and determines if the digits contain
# two adjacent 8s.


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """

    # My solution:
    return str(88) in str(n)

    # Official solution:
    prev_eight = False
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and prev_eight:
            return True
        elif last_digit == 8:
            prev_eight = True
        else:
            prev_eight = False
        n = n // 10
    return False


# Test the function
run_docstring_examples(double_eights, globals(), True)

###############################################################################
