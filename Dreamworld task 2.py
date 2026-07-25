'''
  date: 25/07/2026
  author: Frank Zhang
  description: Dreamworld task 2
  version: 1.0
'''

#Ask for and store the user's height and age
height = float(input("Enter your height in centimeters: "))
age = int(input("Enter your age: "))

if height > 150:
    print("- Stratpsfear, Family Karts, Scorpion Karts")

if height > 120:
    print("- Fearfall , Invader, Corkscrew Roller Coaster, Bumver boats")

if height >90:
    if age >= 5:
        print("- Los Banditos")
    if age >= 8:
        print("- Robot Riot")

if height >80:
    print("- Log Flume, Gold Rush, Family Karts(passenger only), Dogems(passenger only)")

if height <=80:
    if 3<= age <= 8:
        print("- Fortress of Fun (for kids aged 3-8 years)")
    else:
        print("- None of the main rides.")