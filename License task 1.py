'''
  date: 25/07/2026
  author: Frank Zhang
  description: license task 1
  version: 1.0
'''
#Ask for and store the user's name and age
name = input("Enter your name: ")
age = float(input("Enter your age: "))

#Ask for and store the months the user has helod their learner license
months_held = int(input("Enter the number of months you have held your learner license: "))

#Both conditions must be true: age >=16.5 and months_held >= 6
if age >= 16.5 and months_held >= 6:
    print(f"Hello, {name}!")
    print("You are eligible to apply for a full license.")
else:
    print(f"Hello, {name}!")
    print("You are not eligible to apply for a full license.")