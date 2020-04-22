
# coding: utf-8

# # Syntax
# 
# Now that we've seen what regular expressions are, what they're good for, let's get down to business. Learning to use regular expressions is mostly about learning regular expression syntax, the special ways we can characters together to make regular expressions. This notebook will be the bulk of our workshop.

# ## Regular expression syntax<a id='section 1'></a>
# 
# All regular expressions are composed of two types of characters: 
# * Literals (normal characters)
# * Metacharacters (special characters)
# 
# ### Matching characters exactly
# 
# Literals match exactly what they are, they mean what they say. For example, the regular expression `Berkeley` will match the string "Berkeley". (It won't match "berkeley", "berkeeley" or "berkely"). Most characters are literals.
# 
# In the example below, the regular expression `regular` will match the string "regular" exactly.

# In[1]:


import re
pattern = 'regular'
test_string = 'we are practising our regular expressions'
re.findall(pattern, test_string)


# ### Matching special patterns
# 
# Metacharacters don't match themselves. Instead, they signal that some out-of-the-ordinary thing should be matched, or they affect other portions of the RE by repeating them or changing their meaning. For example, you might want find all mentions of "dogs" in a text, but you also want to include "dog". That is, you want to match "dogs" but you don't care if the "s" is or isn't there. Or you might want to find the word "the" but only at the beginning of a sentence, not in the middle. For these out-of-the-ordinary patterns, we use metacharacters.
# 
# In this workshop, we'll discuss the following metacharacters:
# 
# . ^ $ * + ? { } [ ] \ | ( )

# ? Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.
pattern = 'dogs?'
test_string = "I like dogs but my dog doesn't like me."
re.findall(pattern, test_string)

pattern = 'one-?way'
test_string = "Oneway to write oneway is one-way and we may want both variations"
re.findall(pattern, test_string)

#(Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.

pattern = '^the'
test_string = "the best thing about the theatre is the atmosphere"
re.findall(pattern, test_string)


# metacharacters: [ and ] 
# 
# They’re used for specifying a character class, which is a set of characters that you wish to match.

# In[4]:


vowel_pattern = '[ab]'
test_string = 'abracadabra'
re.findall(vowel_pattern, test_string)


# #### Challenge 

# Find all the vowels in the test sentence below.


test_string = 'the quick brown fox jumped over the lazy dog'


# Solution
pattern = '[aeiou]'
re.findall(pattern, test_string)


# ### Ranges
# 
# Characters can be listed individually, or a range of characters can be indicated by giving two characters and separating them by a '-'. For example, `[abc]` will match any of the characters a, b, or c; this is the same as `[a-c]`.
# 
# #### Challenge 
# Find all the capital letters in the following string.

test_string = 'The 44th pPresident of the United States of America was Barack Obama'


# In[10]:


# Solution
pattern = '[A-Z]'
re.findall(pattern, test_string)


# ### Complements
# 
# You can match the characters not listed within the class by complementing the set. This is indicated by including a `^` as the first character of the class; `^` outside a character class will simply match the `^` character. For example, `[^5]` will match any character except `5`.

everything_but_t = '[^t]'
test_string = 'the quick brown fox jumped over the lazy dog'
re.findall(everything_but_t, test_string)[:5]


# #### Challenge 5
# Find all the consonants in the test sentence below.


test_string = 'the quick brown fox jumped over the lazy dog'


# In[14]:


# Solution
pattern = '[^aeiou]'
re.findall(pattern, test_string)[:10]


# #### Challenge 6
# Find all the `^` characters in the following test sentence.

# In[16]:


test_string = """You can match the characters not listed within the class by complementing the set. 
This is indicated by including a ^ as the first character of the class; 
^ outside a character class will simply match the ^ character. 
For example, [^5] will match any character except 5."""


# In[17]:


# Solution
pattern = '\^'
re.findall(pattern, test_string)


# ### Matching metacharacters literally
# 
# Challenge 6 is a bit of a trick. The problem is that we want to match the `^` character, but it's interpreted as a metacharacter, a character which has a special meaning. If we want to literally match the `^`, we have to "escape" its special meaning. For this, we use the `\`.
# 
# #### Challenge 7
# Find all the square brackets `[` and `]` in the following test string

# In[21]:


test_string = "The first metacharacters we'll look at are [ and ]."


# In[27]:


# Solution
pattern = '[\[\]]'
re.findall(pattern, test_string)


# ### Character classes
# 
# The backslash `\` has another use in regexes, in addition to escaping metacharacters. It's used as the first character in special two-character combinations that have special meanings. These special two-character combinations are really shorthand for sets of characters.
# 
# |      Character     |       Meaning      |   Shorthand for  |
# |:------------------:|:------------------:|:----------:|
# |        `\d`        |      any digit     | `[0-9]` |
# |        `\D`        |    any non-digit   |    `[^0-9]`    |
# |        `\s`        |   any whitespace   |    `[ \t\n\r\f\v]`    |
# |        `\S`        | any non-whitespace |    `[^ \t\n\r\f\v]`    |
# |        `\w`        |      any word      |    `[a-zA-Z0-9_]`    |
# | what do you think? |    any non-word    |         `?`   |
# 
# Now here's a quick tip. When writing regular expressions in Python, use raw strings instead of normal strings. Raw strings are preceded by an `r` in Python code. If we don't, the Python interpreter will try to convert backslashed characters before passing them to the regular expression engine. This will end in tears. You can read more about this [here](https://docs.python.org/3/library/re.html#module-re).
# 
# #### Challenge 8
# Find all three digit prices in the following test sentence. Remember the `$` is a metacharacter so needs to be escaped.



test_string = 'The iPhone X costs over $999, while the Android competitor comes in at around $550.'




# Solution
pattern = '\$\d{3}'
re.findall(pattern, test_string)


# ### Repeating things
# 
# Being able to match varying sets of characters is the first thing regular expressions can do that isn’t already possible with the methods available on strings. However, if that was the only additional capability of regexes, they wouldn’t be much of an advance. Another capability is that you can specify that portions of the RE must be repeated a certain number of times.
# 
# | Character |        Meaning        |    Example    |                Matches               |
# |:---------:|:---------------------:|:-------------:|:------------------------------------:|
# |   `{n}`   |    exactly n times    |     `a{3}`    |                 'aaa'                |
# |  `{n, m}` | between n and m times | `[1-9]{2, 4}` |          '12', '123', '1234'         |
# |    `?`    |      0 or 1 times     |   `colou?r`   |           'color', 'colour'          |
# |    `*`    |    0 or more times    |    `data!*`   | 'data', 'data!', 'data!!', 'data!!!' |
# |    `+`    |    1 or more times    |     `lo+l`    |        'lol', 'lool', 'loool'        |
# 
# #### Challenge 9
# Find all prices in the following test sentence.

# In[31]:


test_string = """The iPhone X costs over $999, while the Android competitor comes in at around $550.
Apple's MacBook Pro costs $1200, while just a few years ago it was $1700.
A new charger for the MacBook costs over $80.
"""


# Solution
pattern = '\$\d+'
re.findall(pattern, test_string)


# ### The `re` module in Python
# 
# The regular expression syntax that we've seen so far covers most of the common use cases. Let's take a break from the syntax, and focus on Python's re module. It has some quirks that we should talk about, after which we'll get back to the syntax.
# 
# Up until now we've only used `re.findall`. This function takes two arguments, a `pattern` and a `text` to search through. It returns a list of all the substrings in `text` that follow `pattern`. 
# 
# Two other common functions are `re.match` and `re.search`. These take the same two arguments as `re.findall`. `re.search` looks through `text` for the **first** occurrence of `pattern`. `re.match` only looks at the start of `text`. Rather than returning a list, these two functions return a `match` object, which contains information about the substring in `text` that matches `pattern`. For example, it gives you the starting and ending index of the substring. If no such matching substring is found, they return `None`.

# In[43]:

 
price_pattern = r'\$\d+'
test_string = """The iPhone X costs over $999, while the Android competitor comes in at around $550.
Apple's MacBook Pro costs $1200, while just a few years ago it was $1700.
A new charger for the MacBook costs over $80.
"""
m = re.search(price_pattern, test_string)
m


# The `match` object has everal methods and attributes; the most important ones are `group()`, `start()`, `end()` and `span()`. `group()` returns the string that matched the regex, `start()` and `end()` return the relevant indicies, and `span()` returns the indicies as a tuple.

# In[50]:


print(m.group())
print(m.start())
print(m.end())
print(m.span())


# In general, I prefer just using `re.findall`, because I rarely need the information that `match` object instances give.
# 
# #### Challenge 10
# Write a function called `first_vowel` that takes in a single word, and returns the first vowel. If there is no vowel in the word, it should return the string `"Hey, no vowel!"`.

# In[33]:


# Solution
def first_vowel(word):
    vowel_pattern = r'[aeiou]'
    m = re.search(vowel_pattern, word)
    if m:
        return m.group()
    return 'Hey, no vowel!'


# In[34]:


print(first_vowel('hello'))
print(first_vowel('sky'))


# ### Replacing things
# 
# So far we've just been finding, but I promised you advanced "find and replace"! That's what `re.sub` is for. `re.sub` takes three arguments: a `pattern` to look for, a `replacement` string to replace it with, and a `text` to look for `pattern` in.
# 
# #### Challenge 11
# Replace all the prices in the test string below with `"one million dollars"`.

# In[35]:


test_string = """The iPhone X costs over $999, while the Android competitor comes in at around $550.
Apple's MacBook Pro costs $1200, while just a few years ago it was $1700.
A new charger for the MacBook costs over $80.
"""


# In[36]:


# Solution
pattern = '\$\d+'
re.sub(pattern, 'one million dollars', test_string)


# So far we've used the module-level functions `re.findall` and friends. We can also `compile` a regex into a `pattern` object. The `pattern` object has methods with identical names to the module-level functions. The benefits are if you're searching over huge texts. It's entirely the same as what we've been doing so far so no need to complicate things. But you'll see it around so it's good to know about.

# In[37]:


vowel_pattern = re.compile(r'[aeiou]')
test_string = 'abracadabra'
vowel_pattern.findall(test_string)


# You might also want to experiment with `re.split`.

# #### Challenge 12
# You've received a problematic dataset from a fellow researcher, with some data entry errors/discrepancies. How would you use regular expressions to correct these errors?
# 
# 1. Replace all instances of "district" or "District" with "County". 
# 2. Replace all instances of "Not available" or "[Name] looking up" with numeric codes.  

# In[43]:


import os
DATA_DIR = 'data'
fname = 'problem_dataset.csv'
fname = os.path.join(DATA_DIR, fname)

with open(fname) as f:
    text = f.read()

# Solution

# DO SOME REGEX MAGIC
# cleaned_text = ...
pattern = r'[Dd]istrict'
cleaned_text = re.sub(pattern, 'County', text)

pattern = r'(Not available)|(\[Name\] looking up)'
cleaned_text = re.sub(pattern, '999', cleaned_text)

# with open("data/usecase1/cleaned_dataset.csv", "w") as f:
#     f.write(cleaned_text)


# #### Challenge 13
# Find all words in the following string about robots.

# In[65]:


robot_string = '''Robots are branching out. A new prototype soft robot takes inspiration from plants by growing to explore its environment.

Vines and some fungi extend from their tips to explore their surroundings. 
Elliot Hawkes of the University of California in Santa Barbara 
and his colleagues designed a bot that works 
on similar principles. Its mechanical body 
sits inside a plastic tube reel that extends 
through pressurized inflation, a method that some 
invertebrates like peanut worms (Sipunculus nudus)
also use to extend their appendages. The plastic 
tubing has two compartments, and inflating one 
side or the other changes the extension direction. 
A camera sensor at the tip alerts the bot when it’s 
about to run into something.

In the lab, Hawkes and his colleagues 
programmed the robot to form 3-D structures such 
as a radio antenna, turn off a valve, navigate a maze, 
swim through glue, act as a fire extinguisher, squeeze 
through tight gaps, shimmy through fly paper and slither 
across a bed of nails. The soft bot can extend up to 
72 meters, and unlike plants, it can grow at a speed of 
10 meters per second, the team reports July 19 in Science Robotics. 
The design could serve as a model for building robots 
that can traverse constrained environments

This isn’t the first robot to take 
inspiration from plants. One plantlike 
predecessor was a robot modeled on roots.'''


# In[66]:


# Solution
pattern = r'[Rr]obots?'
re.findall(pattern, robot_string)


# #### Challenge 14
# We can use parentheses to match certain parts of a regular expression.

# In[72]:


price_pattern = pattern = r'\$(\d+)\.(\d{2})'
test_string = "The iPhone X costs over $999.99, while the Android competitor comes in at around $550.50."
m = re.search(price_pattern, test_string)
dollars, cents = m.group(1), m.group(2)
print(dollars)
print(cents)


# Use parentheses to group together the area code of a US phone number. Write a function called `area_code` that takes in a string, and if it is a valid US phone number, returns the area code. If not, it should return the string `"Hey, not a phone number!"`.

# In[62]:


# Solution
def is_valid_number(string):
    string = string.strip()
    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    match = re.search(phone_pattern, string)
    return match is not None

