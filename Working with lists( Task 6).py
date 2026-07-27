'''
  date: 27/07/2026
  author: Frank Zhang
  description: Working with lists (Task 6)
  version: 1.0
'''

def lottery():
    import random  #Imports the random fuction so you can call it later
    names_list = ["Jenna", "Bob", "Tim", "Greg", "Jimmy", "Lisa", "Ralph", "Ben", "Gina"]  #Name lists
    random_number = random.randint(0,len(names_list))  #Returns a random name from the list
    print("The random number is {}".format(random_number))
    print("The lucky number is {}".format(names_list[random_number]))  #Prints the random name from the list

#main program
lottery()  #Calls the lottery function to run the program