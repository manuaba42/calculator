import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def plus(num1, num2):
    total = num1+num2
    print(f"{num1} + {num2} = {total}")
    return total

def minus(num1, num2):
    total = num1-num2
    print(f"{num1} - {num2} = {total}")
    return total

def multi(num1, num2):
    total = num1*num2
    print(f"{num1} * {num2} = {total}")
    return total

def divide(num1, num2):
    total = num1%num2
    print(f"{num1} % {num2} = {total}")
    return total

condi1 = True
while condi1 ==True:
    print(logo)
    first = int(input("What\'s the first number?: "))
    print("+\n-\n*\n%\n")

    condi2 = True
    total = first
    while condi2 == True:
        ope = input('Pick an operation: ')
        next = int(input("What\'s the next number?: "))
        if ope == '+':
            total = plus(total, next)
        elif ope == '-':
            total = minus(total, next)
        elif ope == '*':
            total = multi(total, next)
        elif ope == '%':
            total = divide(total, next)
        

        stage = input("Type 'y' if you want to continue, 'n' if you\n")
        if stage == 'n':
            condi2 = False

    clear = lambda: os.system('clear')
    clear()
    
