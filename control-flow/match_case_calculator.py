

#_ OBJECTIVE: LEARN TO USE MATCH CASE STATEMENTS FOR HANDLING MULTIPLE OPERATIONS IN A SIMPLE CALCULATOR PROGRAM.


#_  DEVELOP A PYTHON SCRIPT NAMED MATCH_CASE_CALCULATOR.PY. THIS CALCULATOR WILL PROMPT THE USER TO ENTER TWO NUMBERS AND SELECT AN OPERATION 
#_ (ADDITION, SUBTRACTION, MULTIPLICATION, OR DIVISION). THE SCRIPT WILL THEN PERFORM THE SELECTED OPERATION USING A MATCH CASE STATEMENT AND DISPLAY THE RESULT.

#! INSTRUCTIONS:

#// MAKE SURE YOU USE NUM1 AND NUM2 FOR FIRST AND SECOND NUMBERS

num1 = int(input('enter the first number:'))  #! ASK THE USER TO INPUT TWO NUMBERS (ONE AT A TIME) USING: “ENTER THE FIRST NUMBER: ” AND “ENTER THE SECOND NUMBER: ”.
num2 = int(input('enter the second number:'))
operator = input('choose the operation (+, -, *, /):') #! ASK FOR THE TYPE OF OPERATION THEY’D LIKE TO PERFORM: “CHOOSE THE OPERATION (+, -, *, /): ”.

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
    case '/' if num2 != 0:
        result = num1 / num2
        print(f'the result is', result)
    case '/' if num2 == 0:
        print('cannot divide by zero')


    

#*FOR ADDITION (+), SUBTRACT (-), MULTIPLY (*), AND DIVIDE (/).

#* DISPLAY THE RESULT OF THE OPERATION IN A USER-FRIENDLY MESSAGE, E.G., “THE RESULT IS [RESULT].”


#_ EXAMPLE INTERACTION:

# ENTER THE FIRST NUMBER: 10
# ENTER THE SECOND NUMBER: 5
# CHOOSE THE OPERATION (+, -, *, /): *
# THE RESULT IS 50.

#* OR, FOR A DIVISION BY ZERO SCENARIO:

# ENTER THE FIRST NUMBER: 10
# ENTER THE SECOND NUMBER: 0
# CHOOSE THE OPERATION (+, -, *, /): /
# CANNOT DIVIDE BY ZERO.


