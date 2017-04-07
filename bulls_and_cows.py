"""
COMS W1002 Sec 001
Homework 2
Bulls and Cows bc module
Author: Gregory V. Cuesta
UNI: gvc2108
Date: 10/10/2016
"""

import random

def generate_secret():
    ''' Generates a 4 digit number with no repeat digits.
    It converts the number to a string and returns it'''

    secretList = random.sample(range(10), 4)
    secretInt = int(''.join(map(str,secretList)))
    secretStr = str(secretInt)
    secret = "{0:0>4}".format(secretStr)
    
    return secret

def how_many_bulls(answer,guess):
    ''' Returns the number of bulls the guess earns when the
    secret number is answer'''
   
    bulls=0
    if guess == answer:
        bulls = 4
    else:
        #add leading 0s to ensure indices are in range
        guess = "{0:0>4}".format(guess)
        
        #count number of bulls by checking matching positions
        if guess[0]==answer[0]:
            bulls = bulls + 1
        if guess[1]==answer[1]:
            bulls = bulls + 1
        if guess[2]==answer[2]:
            bulls = bulls + 1
        if guess[3]==answer[3]:
            bulls = bulls + 1   

    return bulls

def how_many_cows(answer, guess):
    ''' Returns the number of bulls the guess earns when the
    secret number is answer'''
   
    cows=0
    
    #add leading 0s to ensure indices are in range
    guess = "{0:0>4}".format(guess)
    
    #ensure no repeat digits are counted (checks answer against guess)
    for element in answer:
        if element in guess:
            cows = cows + 1

    #ensure no matching bull elements are counted
    if guess[0]==answer[0]:
            cows = cows -1
    if guess[1]==answer[1]:
            cows = cows -1
    if guess[2]==answer[2]:
            cows = cows -1
    if guess[3]==answer[3]:
            cows = cows -1

    return cows