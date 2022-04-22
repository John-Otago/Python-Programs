# This is a Python exercise from Hack in Science called Sets of Love,
# which is essentially is a test of set intersections and differences:
# https://www.hackinscience.org/exercises/sets-of-love

# Instructions:
#
# Sets of love
# Created by Antoine Mazières
# From Pyris, with love.
#
# Once upon a time, in Paris, the city of romance, Bob and Alice met and fall in love with each other.
# To fullfill their romance, they want to meet as much as possible. They share their daily paths among
# Paris districts to know where they can find each other at the same place.
#
# As you know there is 20 districts in Paris:
# {"Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ", "Ⅷ", "Ⅸ", "Ⅹ", "ⅩⅠ", "ⅩⅡ", "ⅩⅢ", "ⅩⅣ", "ⅩⅤ", "ⅩⅥ", "ⅩⅦ",
# "ⅩⅧ", "ⅩⅠⅩ", "ⅩⅩ"}
#
# Exercise 1
# Code a function named love_meet taking bob and alice's daily paths as two lists and returning a set
# of the districts they both visit during the day.
#
# Exercise 2
# Time goes on, and love goes by...
# Alice is bored and get a crush for the strong and handsome Silvester. In order to have an affair with
# Silvester she must find out where both Silvester and her go during the day. But to avoid an unfortunate
# encounter with Bob, she must be sure Bob doesn't go there also. For the sake of her new love, provide
# Alice the function affair_meet that takes Bob, Alice and Silvester daily path in Paris, and returns a
# set of all places where Alice and Silvester can meet and be sure Bob won't be.


# Here are three possible solutions I've come up with:

alice = ['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ']
bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']
silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']


# Solution 1 - a bit clumsy, but works
def love_meet(bob, alice):
    common_set = set(())

    for x in alice:
        if x in bob:
            common_set.add(x)

    return common_set

def affair_meet(bob, alice, silvester):
    possible_set = set(())

    for x in alice:
        if not x in bob and x in silvester:
            possible_set.add(x)

    return possible_set


# Solution 2 - a better one
def love_meet(bob, alice):
    return {x for x in alice if x in bob}

def affair_meet(bob, alice, silvester):
    return {x for x in alice if x in silvester and not x in bob}


# Solution 3 - using Python built-in functions
# See this article and the comments:
# https://dev.to/svinci/intersection-union-and-difference-of-sets-in-python-4gkn
def love_meet(bob, alice):
    return set(alice) & set(bob)

def affair_meet(bob, alice, silvester):
    return (set(alice) & set(silvester)) - set(bob)


# print out the results

print(love_meet(bob, alice))
print(affair_meet(bob, alice, silvester))
