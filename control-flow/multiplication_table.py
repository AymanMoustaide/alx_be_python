
#_OBJECTIVE: USE A FOR LOOP TO GENERATE AND PRINT THE MULTIPLICATION TABLE FOR A GIVEN NUMBER.

#*TASK DESCRIPTION:

# _ THIS SCRIPT WILL ASK THE USER TO ENTER A NUMBER, THEN USE A FOR LOOP TO PRINT THE MULTIPLICATION TABLE FOR THAT NUMBER FROM 1 TO 10.

#! ASK THE USER TO INPUT A NUMBER FOR WHICH THEY WANT TO SEE THE MULTIPLICATION TABLE: “ENTER A NUMBER TO SEE ITS MULTIPLICATION TABLE: ”.
#! SAVE IT IN A VARIABLE NAME NUMBER

x = int(input('ENTER A NUMBER TO SEE ITS MULTIPLICATION TABLE:'))



#* GENERATE AND PRINT THE MULTIPLICATION TABLE:

#! USE A FOR LOOP TO ITERATE THROUGH THE NUMBERS 1 TO 10.
for y in range(1, 11):
    z = x * y #! For each iteration, calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
    print(x, '*', y, '=', z) #! Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.

# Example Interaction:

# If the user inputs 5, the output should be:

# Enter a number to see its multiplication table: 5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50
# This task is designed to reinforce the concept of for loops by applying them in a practical scenario that generates a multiplication table. Through this exercise, students will learn how loops can significantly simplify the process of performing repetitive tasks, enhancing their understanding of looping constructs in Python.