# PPHA 30537
# Spring 2024
# Homework 1

# AttaullahAbbasi
# AttaullahAbbasi12

# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

objects = [1, 'apple', 3.14, True, None]

# For loop 
for index, value in enumerate(objects):
    print(f"The value at position {index} is {value}")

# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

test_strings = [ "radar", "A man, a plan, a canal, Panama!", "Microsoft", "This isn't a palindrome"]

# Loop  each string 
for s in test_strings:
    # Remove non-alphanumeric  and convert to lowercase
    cleaned = ''.join(c for c in s if c.isalnum()).lower()
    # Check 
    if cleaned == cleaned[::-1]:
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')
    
    

# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']

# Infinite loop 
while True:
    # User input
    choice = input('Please pick a vegetable I have available: ').lower()
    # Check
    if choice in available_vegetables:
        print(f'You can have the {choice}.')
        break
    else:
        print('That is not a valid choice, please pick a valid vegetable.')


# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.


# Example 
strings = ['Hello', 'There', 'Apple', 'Banana', 'Cherry', 'avocado']

#  a new list with the required modifications
# The strings are transformed to lowercase unless with an 'a' or 'b',
modified_strings = [s.lower() for s in strings if s[0].lower() not in ['a', 'b']]

# Printing
print(modified_strings)


# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}
short_names = ['IL', 'IN', 'MI', 'WI']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']

# Creating the dictionary 
state_dictionary = {short: long for short, long in zip(short_names, long_names)}

# Printing 
print(state_dictionary)


#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

# Defining function
def sum_evaluate(a, b):
    total = a + b
    if total > 10:
        return "big"
    elif total == 10:
        return "just right"
    else:
        return "small"

#  tuples
start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

# Apply the function to  tuples
result_list = [sum_evaluate(a, b) for a, b in start_list]

# Printung
print(result_list)



# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

# Define the function

def my_func(a):
    b = 40
    return a + b

# Call 
x = my_func(10)



# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
#import random
#from numpy import random

import random

# Define the function
def generate_password(length, special_chars=True, include_numbers=True):
    if not 8 <= length <= 16:
        print("Length must be between 8 and 16.")
        return

    # Define the characters
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_numbers:
        characters += "0123456789"
    if special_chars:
        characters += "!@#$%^&*"

    # Generate 
    return ''.join(random.choice(characters) for _ in range(length))

# Example 
print(generate_password(12))



# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.


# Define the class
class MovieDatabase:
    def __init__(self, creator_name):
        self.creator_name = creator_name
        self.movies = []

    def add_movie(self, name, genre, rating):
        self.movies.append({'name': name, 'genre': genre, 'rating': rating})

    def what_to_watch(self):
        if not self.movies:
            print("No movies in database.")
            return
        movie = random.choice(self.movies)
        print(f"Tonight, courtesy of {self.creator_name}, watch '{movie['name']}'! "
              f"It's a {movie['genre']} rated {movie['rating']}/5.")

# Create  instance and add movies
my_database = MovieDatabase("YourName")
my_database.add_movie("Movie1", "comedy", 4)
my_database.add_movie("Movie2", "drama", 5)
my_database.add_movie("Movie3", "horror", 3)
my_database.add_movie("Movie4", "action", 5)

# Call 
my_database.what_to_watch()


#Some  help e was taken from OpenAI. 2024. "ChatGPT-3.5." Accessed [7th April, 2024]. https://openai.com/