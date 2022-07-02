# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 11:23:33 2022

@author: vucen
"""
"""
text = input("Type something...")

print(text * 3)

print("hello")

"""
"""
PSET1 - Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

s = "abcbcd"
longest = 0
current_length = 0
current_word = ""
longest_word = ""

if len(s) != 0:
    longest = 1
    current_length = 1
    current_word = s[0]
    longest_word = s[0]

for i in range(len(s) - 1):
    if s[i] <= s[i+1]:
        current_length += 1
        current_word += s[i+1]
        if current_length > longest:
            longest = current_length
            longest_word = current_word
    else:
        current_length = 1
        current_word = s[i+1]    
    
print("Longest substring in alphabetical order is:", longest_word)

"""

"""

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) 
and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.
...
Game over. Your secret number was: 83

low = 0
high = 100
response = ""
ans = int((low + high) / 2)

print("Please think of a number between 0 and 100!")
while response != "c":
    print("Is your secret number", ans, end="")
    print("?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if response == "h":
        high = ans
        ans = int((low + high) / 2)
    elif response == "l":
        low = ans
        ans = int((low + high) / 2)
    elif response == "c":
        break
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was:", ans)

"""

"""
FACTORIAL RECURSIVELY

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))

"""

"""
ITERATIONAL POWER

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    for i in range(1, exp + 1):
        result *= base

    return result

"""


"""
RECURSIVE POWER

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)
"""

"""
gcd iter

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
        test_value = a
    else:
        test_value = b


    while a % test_value != 0 or b % test_value != 0:
        if test_value != 1:
            test_value -= 1

    return test_value

print(gcdIter(17, 12))

"""

"""
gcd recur

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


print(gcdRecur(6, 12))

"""

"""
Exercise: is in 

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    # Your code here
    # Base code for empty string
    if aStr == "":
        return False
    # Base code for if we only have one letter left
    elif len(aStr) == 1:
        return char == aStr

    mid_index = len(aStr) // 2
    mid_char = aStr[mid_index] 

    # Base code for when it is the middle char
    if char == mid_char:
        return True
    # Rest of the cases
    elif char < mid_char:
        return(isIn(char, aStr[:mid_index]))
    else:
        return(isIn(char, aStr[mid_index + 1:]))



print(isIn('b', 'bceejlnoopsstuuxyzz')) 

"""

"""
Write a procedure called oddTuples, which takes a tuple as input, 
and returns a new tuple as output, where every other element of the input tuple is copied, 
starting with the first one. 
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple'). 

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newtup = ()
    for i in range(0, len(aTup), 2):
        newtup += (aTup[i], )
    
    return newtup

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))

"""

"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    for key in aDict.keys():
        for value in aDict[key]:
            result += 1

    return result

print(how_many(animals))


"""

"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    most_values = 0
    most_values_key = None
    for key in aDict.keys():
        if len(aDict[key]) >= most_values:
            most_values = len(aDict[key])
            most_values_key = key

    return most_values_key


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest({'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}))



"""

"""


def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

print(fancy_divide([0, 2, 4], 0))

"""

