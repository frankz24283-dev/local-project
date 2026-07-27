'''
  date: 27/07/2026
  author: Frank Zhang
  description: Working with lists (Task 5)
  version: 1.0
'''

#Import the 'shuffle' function from the 'random' module, which is used for shuffling the elements.
from random import shuffle

#Create a list 'color' with several color strings
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#Use the 'shuffle' function to randomly shuffle the elements of the 'color' list
shuffle(color)

#Print the shuffled list of colors, which will have its elements in a random order
print(color)