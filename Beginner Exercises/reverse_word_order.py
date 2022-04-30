#########################################################################################################################

# Practice Python
# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

# Reverse Word Order
# strings

# Exercise 15
#
# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the 
# user the same string, except with the words in backwards order. For example, say I type the string:
#
#   My name is Michele
#
# Then I would see the string:
#
#   Michele is name My
#
# shown back to me.

#########################################################################################################################

# Solution 1:

print(" ".join(list(input("Enter text: ").split()[::-1])))

# Solution 2:

print(" ".join(reversed(list(input("Enter text: ").split()))))

# Solution 3:

print(*list(input("Enter text: ").split()[::-1]))

#########################################################################################################################

# Breakdown of the two Solutions above:

input = input("Enter text: ")
mylist = list(input.split())

# Solution 1
s1 = " ".join(mylist[::-1])
print(s1)
      
# Solution 2
s2 = " ".join(reversed(mylist))
print(s2)

# Solution 3
print(*mylist[::-1])

#########################################################################################################################
