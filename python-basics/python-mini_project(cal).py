first = int(input("Enter First Number: "))
operator = input("Enter Operator (+, -, *, /, %): ")
second = int(input("Enter Second Number: "))

'''
first = int(first)
second = int(first)
'''

if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '/':
    print(first / second)
elif operator == '*':
    print(first * second)
elif operator == '%':
    print(first % second)
else:
    print("Invalid Operation")