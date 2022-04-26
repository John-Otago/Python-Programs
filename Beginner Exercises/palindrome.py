############################################################################
# Check for palindrome
#
# - Palindrome seems to be a common exercise for beginner programmers, which
#   seems to be easy but can be tricky when you dig deeper into it.
#
# - This Python script contains several possible solutions, as well as their
#   potential limits, plus relevant discussions and resources.

# What are palindromes? See this video: https://youtu.be/EA2DKe8-IYg
# For "palindrome numbers", see this: https://youtu.be/OKhacWQ2fCs

############################################################################

# I first saw this exercise in Swaroop's book A Byte of Python (ABP), p.76.
#
# Swaroop has offered a sample program that can check if an input is a
# palindrome, but it won't work with any input that involves punctuations,
# spaces, or uppercase letter--hence he challenges the readers to improve
# the program.

# I then came across this issue in John V. Guttag's book Introduction to
# Computation and Programming Using Python (3rd Edition, MIT Press, 2021;
# hereafter ICPUP), which comes from the popular MIT open course on this
# subject: https://ocw.mit.edu/6-0001F16

# In this script, I try to tackle the palindrome problem with my own twist,
# offering a few solutions while addressing some of the issues in the books
# above.

############################################################################
############################################################################

# Solution 1
# Based on Swaroop's program in ABP (p.76), solving the challenge that he
# set for the readers. It also prints out each step it takes to solve the
# challenge.


# Things we need to know for this solution:
# Remove punctuations from a string: https://datagy.io/python-remove-punctuation-from-string/
# Remove spaces from a string: https://www.journaldev.com/23763/python-remove-spaces-from-string
# Change everything to lower case, too (using str.lower).

import string

def reverse(text):
    return text[::-1]

def is_pal(text):
    return text == reverse(text)

something = str.lower(input("Enter text (Solution 1): "))
phrase1 = something.translate(str.maketrans("", "", string.punctuation))
phrase2 = phrase1.replace(" ", "")

print(phrase1)
print(phrase2)

if is_pal(phrase2):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

############################################################################

# Solution 2:
# John Guttag's solution in ICPUP, Chapter 6, Figure 6-4, p.119.
# In ICPUP, this part is mainly to demonstrate the concept of 'recursion'.

# The code is on GitHub: https://github.com/guttag/Intro-to-Computation-and-Programming/tree/main/code/chapter%2006
# ... and also explained in Eric Grimson's YouTube video: https://youtu.be/KcgxogTU3Z8
# His full video on Recursion and Dictionaries is here: https://www.youtube.com/watch?v=WPSeyjX1-4s

def is_palindrome(s):
    """Assumes s is a str
    Returns True if letters in s form a palindrome; False
    otherwise. Non-letters and capitalization are ignored."""

    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))

print(is_palindrome(input("Enter text (solution 2): ")))
# slightly modified here to take an input from the user

############################################################################
# Solution 3 - my own solution inspired by both Swaroop and Guttag

import string

text = str.lower(input("Enter text (Solution 3): "))

def is_palin(text):
    letters = ""
    for x in text:
        if x in string.ascii_lowercase:
            letters += x
    return letters == letters[::-1]

print(is_palin(text))

############################################################################
############################################################################

# You can test all three solutions with the following strings, which should
# all return True or "Yes, it is a palindrome":
#
# Eve
# Wow, wow.
# Rise to vote, sir.
# racecar
# 101 (This returns None in Solution 2 & 3, evaluated as True. See below.)
# 100aaa001 (This returns 'aaa' in Solution 2 & 3, then True. See below.)

# Test other strings, which should all return False or "No, it is not a
# palindrome"
#
# abc
# Hello!
# aqopl239can2v39n/mal.3's93nncv1fcgcgslx9023

# The next few are a bit tricky--Solution 1 will return the correct value
# (False), but Solution 2 & 3 will fail:
#
# 191aa076
# 9328nnn902010
# 25117abba80

# Also, if you enter a non-palindrome number, like 2022393820, then both
# Solution 2 and 3 will incorrectly return True! This is because a number
# won't be added to the string "letters" in these Solutions, and we will
# get "letters = None" that is still evaluated as True in Solution 2 and 3.

# Similarly, if you enter nothing (input = None), then all three Solutions
# will return True. 

# In Eric Grimson's video mentioned above, he does say that an empty string
# can be considered a palindrome, in the sense that a reversed empty string
# is still empty (same as itself).

############################################################################
############################################################################

# Solution 4
# This is a modified version of Solution 3, which works for words/phrases as
# well as non-palindrome numbers (like 2022393820).

# For palindrome numbers (e.g. 101), this version will actually check the
# number and return True, unlike Solution 2 and 3 that will return None and
# evaluate None as True (which is not really checking the number and hence
# won't work for non-palindrome numbers as explained above).

import string

text = str.lower(input("Enter text (Solution 4): "))

def is_palin(text):
    letters = ""
    for x in text:
        if x in string.ascii_lowercase:
            letters += x
        elif x in string.digits: # added to check for numbers
            letters += x
    return letters == letters[::-1]

print(is_palin(text))

############################################################################
############################################################################

# Conclusion:

# All Solutions included here can check if a word/phrase is a palindrome, 
# but only Solution 1 and 4 can check if a number (like "2022393820") is a
# palindrome number.

# Mixed strings of letters and digits are a bit more complicated:
# 
# 100aaa001 -> all Solutions return the right result, but see # line 126
# 191aa076 -> Solutions 2 & 3 will fail
# 9328nnn902010 -> Solutions 2 & 3 will fail
# 25117abba80 -> Solutions 2 & 3 will fail
# afh87932uhdf9y93 -> all Solutions return the right result 

# Solution 4 is my preferred approach.

############################################################################
############################################################################

# [Edited to add]
# There's another solution in ICPUP (Chapter 8, p.164), available at
# https://github.com/guttag/Intro-to-Computation-and-Programming/tree/main/code/chapter%2008

# Here's the code:

# # Code from page 164
# def is_pal(x):
#     """Assumes x is a list
#         Returns True if the list is a palindrome; False otherwise"""
#     temp = x[:]
#     temp.reverse()
#     return temp == x
#
# def silly(n):
#     """Assumes n is an int > 0
#         Gets n inputs from user
#         Prints 'Yes' if the sequence of inputs forms a palindrome;
#             'No' otherwise"""
#     result = []
#     for i in range(n):
#         elem = input('Enter element: ')
#         result.append(elem)
#     print(result)
#     if is_pal(result):
#         print('Yes')
#     else:
#         print('No')
#
# silly(2)

# I've modified the code to take an input (a full string) directly from the
# user. Let's call it Solution 5:

def is_pal():
    """Assumes x is a list
        Returns True if the list is a palindrome; False otherwise"""
    x = list(input("Enter text (Solution 5): "))
    temp = x[:]
    temp.reverse()
    # print(temp)
    # print(x)
    print(temp == x)

is_pal()

# Pro:
# It handles non-palindrome numbers and mixed strings pretty well.
# Cons:
# It can't handle punctuations (like "Wow, wow." or "Rise to vote, sir.")
# It can't handle capital letters ("Eve" or "Wow" will both return False).

# Discussion
# In linguistics, both "Wow, wow." and "Rise to vote, sir." should count as
# palindrome phrases, as punctuations are not counted. "Eve" should also be
# a palindrome, if we ignore whether a letter is in upper or lower case.

# In programming, technically a capital letter is not equal to a lower-case
# letter, which means "Eve" is not the same as "eve" (hence the former is
# not a palindrome). The same can be said about punctuation.

# Previous solutions will all check for lower-case letters and will remove
# punctuations. Solution 5 (in its current form) won't. It needs a couple of
# changes to work in the same way as previous solutions--or it can stand
# alone in its own league to show a slightly different understanding of
# palindrome (the machine version rather than the human version).

############################################################################
############################################################################
