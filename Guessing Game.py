
import random
import math

num_guesses = 0
print('Hello! What is your name?: ')
myName = input()

number = random.randint(1,50)
print(myName + ", guess a number between 1 and 50. You can make 5 guesses.")

while num_guesses < 6:
    print('Take a guess: ')
    guess = input()
    guess = int(guess)
    
    num_guesses += 1
    
    if guess < number:
        print('Your guess is too small!')
    elif guess > number:
        print('Your guess is too big!')
    elif guess == number:
        break

if guess == number:
    num_guesses = str(num_guesses)
    print("Congrats " + myName + ", you guessed the correct number in " + num_guesses + " tries!")

if guess != number:
    number = str(number)
    print("The number was " + number + ". Better luck next time!")
