'''
  date: 26/07/2026
  author: Frank Zhang
  description: Guessing Game task 3
  version: 1.0
'''


import random

#Ask the user to enter their name
name = input("Enter your name: ")

#Generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)

guess_count = 0

# Start a loop to keep asking until they guess correctly 
while True:
    guess = int(input( f"Hello, {name}! Guess a number between 1 and 10: "))
    guess_count += 1
    if guess == secret_number:
        print(f"Congratulations, {name}! You guessed the number in {guess_count} tries.")
        break
    else:
        print("Too high! Try again.")