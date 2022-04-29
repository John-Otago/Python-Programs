#####################################################################################################################################

# Practice Python: Beginner Python exercises
# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

# Exercise 3 (and Solution)

# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:
#     1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and
#        print out this new list.
#     2. Write this in one line of Python.
#     3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that
#        number given by the user.

#####################################################################################################################################

# My solution 1:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

user_num = int(input("Please enter a number: "))

print([i for i in a if i < user_num])

#####################################################################################################################################

# My solution 2

# It's not specified in the briefing, but in the Official Solution there's an un-ordered list ("b") for Extra Exercise 3, and the 
# output must be an ordered list--hence this new solution:

b = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11]

user_num = int(input("Please enter a number: "))

print(sorted(i for i in b if i < user_num))

#####################################################################################################################################
