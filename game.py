import bulls_and_cows as bc 

def main():

    print('Welcome to Bulls and Cows!')
    again = 'yes'
    while (again == 'yes'):
          play_game()
          again = input('Would you like to play again? (yes/no)')
    print('Bye!')

def play_game():

    guess = 0
    attempts = 0
    answer = bc.generate_secret()
  
    while not(bc.how_many_bulls(answer, guess) == 4):
        guess = input("Guess a four digit number: ")
        
        # ensure guess is 4 digits
        if len(guess) == 4:
            bc.how_many_bulls(answer, guess)
            bc.how_many_cows(answer, guess)
            
            # shows player their current bulls and cows counts
            print("Your number", guess, "has", bc.how_many_bulls(answer, guess), \
            "bulls and", bc.how_many_cows(answer, guess), "cows.")
            
            # keep track of attempts
            attempts = attempts + 1
        else:
            print("That wasn't four digits. Attention to detail goes a long way! Try again.")
            
    if attempts == 1:
        print("You guessed correctly on your first try. Stop cheating, cheater.")
    else:
        print("Finally! It took you", attempts,"attempts. You suck!")

# call the main function to run the game
main()
