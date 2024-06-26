
num1 = int(input('Enter the first number:'))  
num2 = int(input('Enter the second number:'))
operator = input('Ehoose the operation (+, -, *, /):') 

match operator: 
    case '+':
        result = num1 + num2
        print(f'the result is', result)
    case '-':
        result = num1 - num2
        print(f'the result is', result)
    case '*':
        result = num1 * num2
        print(f'the result is', result)
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f'the result is', result)
        else:
            print('cannot divide by zero')