# Exercise on HackInScience: Longest Word
# https://www.hackinscience.org/exercises/longest-word


def longest_word(text):
    d = {}
    for x in text.split():
        d.update({x: len(x)})    
    return max(d, key=d.get) # I like this :)

# longest_word(text)


# This can pass the exercise, but it won't work if two 
# words in a string are both the longest word, such as
# text = "Complimentary and complementary are both the
# longest words in this string."

# In this case, "complimentary" and "complementary" are
# both 13 characters, yet the function will only return
# one of them.

# Punctuations are also included in the split strings,
# so for example "word," and "words" will both be 
# treated as 5 characters.

# I may revisit this exercise to develop a better 
# solution in the future.
