# Notes for Ch 1 -
# 1. Short introduction to Programming in Python

# Print -------------------------------------------------------------------
# Using print() is the only way to show the output when running an
# entire script
text = "Data Carpentry"
# This line will show if run individually, but not when entire
# script is run
text

# This line will show when entire script is run
print(text)

# Lists -------------------------------------------------------------------
# Lists hold ordered sequence of elements
numbers = [1, 2, 3]
numbers[0] # first element is 0th

# Can use for loop to access elements in list:
for num in numbers:
    print(num)

# Can add elements to end of a list using append()
# Invoke 'method' using . followed by method and arguments
numbers.append(4)
print(numbers) # now we've added 4 to the numbers list

# Examine available methods for an object with help()
#help(numbers)

# Tuples -------------------------------------------------------------------
# Similar to list except immutable (can't be changed) 
a_tuple = (1, 2, 3) # regular parentheses instead of brackets
b_tuple = ('blue', 'green', 'red')

a_tuple

# Dictionaries  -------------------------------------------------------------
# Hold pairs of objects - instead of indexing a list based on the position
# you can access the values with keys (names or unique identifiers for each)
rev = {'first': 'one', 'second':'two'}
rev['first']

#Add item by assigning value to a new key:
rev['third'] = 'three'
rev

# For loops with dictionaries is more complicated:
for key in rev.keys():
    print(key, '->', rev[key])

# another option:
for key, value in rev.items():
    print(key, '->', value)

# update dictionary so that second reads 2 instead of second
rev['second'] = 2
rev

# Functions ---------------------------------------------------------------
# Define function using def keyword
def add_function(a, b):
    result = a + b
    return result

z = add_function(20, 22)
print(z)

