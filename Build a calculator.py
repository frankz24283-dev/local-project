'''
  date: 29/07/2026
  author: Frank Zhang
  description: Build a calculator
  version: 1.0
'''
#------functions------
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def main():
    num1 = 0
    num2 = 0
    answer = 0
    op = ''

    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a number: '))
    op = input('Enter your operation, + - * /:')

    if(op == '+'):
        answer = add(num1,num2)
        print(f'{num1}+{num2}={answer}')
    elif(op == '-'):
        subtract(num1,num2)

#-----main routine-------
if(__name__== "__main__"):
    main()