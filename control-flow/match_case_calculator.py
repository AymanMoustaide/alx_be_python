
num1 = int(input('enter the first number:'))  
num2 = int(input('enter the second number:'))
operation = input('choose the operation (+, -, *, /):')

match operation: 
    case '+':
        result = num1 + num2
        print(f'The result is {result}.')
    case '-':
        result = num1 - num2
        print(f'The result is {result}.')
    case '*':
        result = num1 * num2
        print(f'The result is {result}.')
    case '/':
        if num2 != 0:
            result =num1 / num2
            print(f'The result is {result}.')
        else:
            print('Cannot divide by zero.')
#D