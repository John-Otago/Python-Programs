##########################################################################################################################################

# Practice Python: Beginner Python exercises
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Exercise 1
#
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year 
# that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore
# be out of date the next year). If you want to do this in a generic way, see exercise 39.
#
# Extras:
#
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button).

##########################################################################################################################################

# My solution (to all questions including the "extras"):

def cent(name, age):
    print(f"Hello {name}, you will be 100 in {2022 - age + 100}.\n" * copies)
    # change "2022" to the year that you are doing this exercise

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
copies = int(input("How many times would you like to see the result? "))

cent(name, age)

##########################################################################################################################################

# Official solution (only to the initial question, but not the "extras"):
# https://www.practicepython.org/solution/2014/02/05/01-character-input-solutions.html

##########################################################################################################################################
