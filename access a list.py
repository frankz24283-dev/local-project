'''
  date: 29/07/2026
  author: Frank Zhang
  description: access a list
  version: 1.0
'''
import random
def lottery():
    name_list = ["Jenna", "Bob", "Tim", "Greg", "Jimmy", "Lisa", "Ralph", "Ben", "Gina"]
    random_number = random.randint(0, len(name_list) - 1)
    print("The random number is {}".format(random_number))
    print("The lucky winner is {}".format(name_list[random_number]))
lottery()