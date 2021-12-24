'''
Author - Harsh Singhania
SSW 540 - Assignment 4: Guess a Number using loops and a function
Creating a python program for user to guess the number the computer chooses at random. The user gets 6 tries to guess the number. 
'''

import random
guessesTaken = 0
print('Hello! What is your name?')
myName = input()
number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    """Taking 6 number of guesses from user and comparing with random number the computer chose. Handled both exceptions of when user enter a non-integer values
    and values < 1 and > 20."""
    try:
        print('Take a guess.')
        guess = input()
        guess = int(guess)
    except:
        print("Please enter integer values only. Try Again!")
        continue
    if guess>1 and guess<21:
        guessesTaken = guessesTaken + 1
        if guess < number:
            print('Your guess is too low.') .
        if guess > number:
            print('Your guess is too high.')
        if guess == number:
            break
    else:
        print("Please enter values between the range 1-20 only.")
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Sorry you are out of turns to guess. The number I was thinking of was ' + number)
