# This is a dice game, the user throws a dice, 
# the game consists of three trials to guess the dice value. If the
# user guesses the value correctly within the trials then the user wins. 
# After the trials, the game ends and the user loses the game.
import random 

def play_dice_game():
   print("Welcome to the dice game!")
   print("You will be given three chances to guess the dice value.")

   # Generate a random number between 1 and 6 for the dice
   dice_value = random.randint(1, 6)

   # Start the game with three trials
   for trial in range(1, 4):
       print(f"Trial {trial}: Guess the dice value (1-6):")
       user_guess = int(input())
       initialTries = 3 - trial  # Update the remaining trials value for each trial
       print(f"You have {initialTries} tries left.")

       if user_guess == dice_value:
         print("Congratulations! You guessed the correct value.")
         return True
       if initialTries == 0:
            print(f"Sorry you lost the game. The dice value was {dice_value}.")
            return False

play_dice_game()

