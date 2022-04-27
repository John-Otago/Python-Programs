# An exercise at HackInScience:
# https://www.hackinscience.org/exercises/sort-students

# Sort students
# Created by Antoine Mazières
 
# This is a triple exercise, it's an introduction to sorting lists in Python.

# Exercise 1
# Write a function sort_a_list that takes a list as argument and return the list sorted in the descending order, such as:
# 
# >>> sort_a_list([1, 3, 2, 4, 6, 5, 9, 7])
# [9, 7, 6, 5, 4, 3, 2, 1]
# 
# Beware, I'll test it with other types, not only integers! But always with list of elements of the same type.

# Exercise 2
# Given a list where each element is a pair of a mark, and a student name, such as:
# 
# >>> my_class = [(85, 'Susan Maddox'), (6, 'Joshua Tran'), (37, 'Jeanette Wafer')]
# 
# Write a function named sort_by_mark that take as argument a similar list and returns it sorted by mark in descending order. Such as:
# 
# >>> sort_by_mark(my_class)
# [(85, 'Susan Maddox'), (37, 'Jeanette Wafer'), (6, 'Joshua Tran')]

# Exercise 3
# Write a function named sort_by_name that take as argument a similar list and returns it sorted by name in ascending order, such as:
# 
# >>> sort_by_name(my_class)
# [(37, 'Jeanette Wafer'), (6, 'Joshua Tran'), (85, 'Susan Maddox')]

############################################################################

# My solution:

def sort_a_list(a_list):
    return sorted(a_list, reverse=True)

def sort_by_mark(my_class):
    def take_mark(my_class):
        return my_class[0]
    return sorted(my_class, reverse=True, key=take_mark)

def sort_by_name(my_class):
    def take_name(my_class):
        return my_class[1]
    return sorted(my_class, key=take_name)

############################################################################  

# To test: uncomment the following lines:

# print(sort_a_list([3, 2, 1]))

# my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]

# print(sort_by_mark(my_class))
# print(sort_by_name(my_class))
