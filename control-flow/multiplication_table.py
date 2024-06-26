
#_OBJECTIVE: USE A FOR LOOP TO GENERATE AND PRINT THE MULTIPLICATION TABLE FOR A GIVEN NUMBER.

x = int(input('ENTER A NUMBER TO SEE ITS MULTIPLICATION TABLE:'))

#* GENERATE AND PRINT THE MULTIPLICATION TABLE:

#! USE A FOR LOOP TO ITERATE THROUGH THE NUMBERS 1 TO 10.

for y in range(1, 11):
    z = x * y #! For each iteration, calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
    print(x, '*', y, '=', z) #! Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.