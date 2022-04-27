########################################################################################
# Exercise at HackInScience:
# https://www.hackinscience.org/exercises/print-sorbet-flavors

# Print sorbet flavors
# Created by Julien Palard
# 
# You're working for a restaurant and they're asking you to generate the sorbet menu.
# Provide a script printing every possible sorbet duos from a given list of flavors.
# Don't print recipes with twice the same flavor (no "Chocolate Chocolate"), and don't 
# print twice the same recipe (if you print "Vanilla Chocolate", don't print "Chocolate
# Vanilla", or vice-versa).
# 
# The flavors are:
# 
# FLAVORS = [
#     "Banana",
#     "Chocolate",
#     "Lemon",
#     "Pistachio",
#     "Raspberry",
#     "Strawberry",
#     "Vanilla",
# ]
# 
# Print one duo per line, and separate flavors by comas, so your output should look like:
# 
# Banana, Chocolate
# Banana, Lemon
# Banana, Pistachio
# Banana, Raspberry
# Banana, Strawberry
# Banana, Vanilla
# Chocolate, Lemon
# …

########################################################################################

# Solution 1 - the easiest method

for i in FLAVORS:
    for j in range(FLAVORS.index(i)+1, len(FLAVORS)):
        print(f"{i}, {FLAVORS[j]}")

########################################################################################

# Solution 2 - create a copy list

flavors_copy = FLAVORS.copy()

for i in flavors_copy:
    for j in FLAVORS:
        if i != j:
            print(f"{i}, {j}")
    FLAVORS.remove(i)

########################################################################################
