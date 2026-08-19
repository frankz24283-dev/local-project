'''
   author: Frank Zhang
   date: 19/08/2026
   version: 1.0
   description: Guess a number between 1-100
'''

#-------libraries---------
import random
#------functions---------
def list_number():
    random_number = []
    #creat a list of numbers
    for i in range(1,101):
        random_number.append(i)
    return random_number
#------main routine------

if(__name__=="__main__"):
    #Intro the game
    print("Welcome to my gueesing game")
    #Enter your name
    name = str(input("Enter your name: "))
    #Enter your age
    age = int(input("Enter you age: "))
    #Make a list of number and pick a random number
    list_numbers = list_number() # It will make a list of numbers from 1-100
    # intro to the game
    #computer random number
    random_number = random.choice(list_numbers)
    # give feedback if higher or lower
    #count amount of guesses
    guess_count = 0
    guess = 0
    # Give the stats how it took to guess
    while guess != random_number