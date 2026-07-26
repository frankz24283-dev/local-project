'''
  date: 26/07/2026
  author: Frank Zhang
  description: Working with lists (Task 3)
  version: 1.0
'''
#This is a list, lists always start counting from 0
student_list = ["Jenna", "Bob", "Tim", "Greg", "Jimmy"]

count = 0 #Creat a count
while count < len(student_list):  #while 0 is less than the length of the list
    print(count, student_list[count])  #print a number, access the list
    count += 1  #the count must increment by 1 to acess the next name on the list
print("That is all of the students.")