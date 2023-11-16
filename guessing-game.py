# handle user guesses
#   if they guess correct, tell them they won
#   otherise tell them if they are too high or too low
# BONUS - let player play again if they want
import random

random_number = random.randint(1,11)
guess = None


while guess != random_number:
    guess = input('Pick a number from 1 to 10: ')
    guess = int(guess)
    if guess < random_number:
        print('Too low!')
    elif guess > random_number:
        print('Too high!')
    else: 
        print('You got it!')
    

print(random_number)