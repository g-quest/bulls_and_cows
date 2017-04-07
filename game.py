"""
COMS W1002 Sec 001
Homework 2
Bulls and Cows game module
Author: Gregory V. Cuesta
UNI: gvc2108
Date: 10/10/2016
"""

import bulls_and_cows as bc ##this means you only have to write bc.function instead
# of bulls_and_cows.function

def main():
# Do not change this function!
    print('Welcome to Bulls and Cows death match!')
    again='y'
    while (again=='y'):
          play_game()
          again=input('would you like to play again? (y/n)')
    print('So long sucker!')


def play_game():
    ''' Plays one interactive game of bulls and cows on the console'''

    guess = 0
    attempts=0
    answer = bc.generate_secret()
    #print(answer) #uncommenting shows answer to help with debugging
  
    #establish a while loop for the game  
    while not(bc.how_many_bulls(answer, guess) == 4):
        guess = input("Guess a four digit number: ")
        
        #ensure guess is 4 digits
        if len(guess) == 4:
            bc.how_many_bulls(answer, guess)
            bc.how_many_cows(answer, guess)
            
            #shows player their current bulls and cows counts
            print("Your number", guess, "has", bc.how_many_bulls(answer, guess), \
            "bulls and", bc.how_many_cows(answer, guess), "cows.")
            
            #keep track of attempts
            attempts=attempts+1
        else:
            print("That wasn't four digits. Attention to detail goes a long way. Try again.")
            
    if attempts ==1:
        print("You guessed correctly on your first try. Stop cheating, cheater.")
    else:
        print("Finally! It took you", attempts,"attempts. You suck!")

#call the main function to run the game
main()
