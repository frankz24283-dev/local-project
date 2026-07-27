'''
  date: 27/07/2026
  author: Frank Zhang
  description: Working with lists (Task 7)
  version: 1.0
'''
shopping_list = [] #enmpty list
item = 0 #you have to define the item in order for the loop to execute
print("This program will remember your shopping list")
while item != "":
    item = input("Please type in each item for your shopping list: \n Press enter to complete the list and view your shopping list")
    shopping_list.append(item)
print("Here is your items on your list:")
for i in shopping_list: #prints every item in your list
    print(i)