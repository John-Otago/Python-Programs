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

print(" ".join(input("Enter text: ").split()[::-1]))

# Solution 2:

print(" ".join(reversed(input("Enter text: ").split())))

# Solution 3:

print(*input("Enter text: ").split()[::-1])

# Solution 4
print(*reversed(input("Enter text: ").split()))

#########################################################################################################################

# Breakdown of the two Solutions above:

input = input("Enter text: ")
mylist = input.split()

# Solution 1
s1 = " ".join(mylist[::-1])
print(s1)
      
# Solution 2
s2 = " ".join(reversed(mylist))
print(s2)

# Solution 3
print(*mylist[::-1])

# Solution 4
print(*reversed(mylist))

#########################################################################################################################

# Comments:

# In the breakdown, "input.split()" will return a list of split items from the "input" string.
# This list of split items is then temporarily stored in a variable called "mylist". 
# 
# Solution 1 & 2 both use ".join" to turn the content of a list ("mylist") into a string.
# Solution 3 & 4 both use "*" (star/asterisk) to unpack the iterable sequence "mylist" and return the content from it.
# 
# Both methods can eventually help print out a string of reversed items from "mylist" (the split input).

# I got the inspiration for Solution 3 & 4 when I was looking for something else and stumbled upon "sequence unpacking":
# https://stackoverflow.com/questions/52230513/python-how-to-remove-last-comma-from-printstring-end

# See this video for more on Sequence Unpacking with Asterisk Operators in Python:
# https://youtu.be/K5XHaoROxI4

# Overall, I prefer Solution 3 & 4, although the first two are also good.

#########################################################################################################################
