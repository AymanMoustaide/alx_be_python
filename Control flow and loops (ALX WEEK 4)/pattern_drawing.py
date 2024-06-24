
#_DRAWING PATTERNS WITH NESTED LOOPS

#* OBJECTIVE: UTILIZE WHILE LOOPS AND NESTED FOR LOOPS TO DRAW A SIMPLE TEXT-BASED PATTERN.

#_ DEVELOP A PYTHON SCRIPT NAMED PATTERN_DRAWING.PY. THIS SCRIPT WILL PROMPT THE USER TO ENTER A POSITIVE INTEGER, 
#_ THEN USE NESTED LOOPS TO PRINT A SQUARE PATTERN OF THAT SIZE MADE OF ASTERISKS (*).

#! INSTRUCTIONS:

# #! ASK THE USER TO INPUT A POSITIVE INTEGER THAT REPRESENTS THE SIZE OF THE PATTERN (I.E., THE LENGTH OF EACH SIDE OF THE SQUARE): “ENTER THE SIZE OF THE PATTERN: ”.
size = int(input('ENTER THE SIZE OF THE PATTERN:'))

# #! DRAW THE PATTERN:
tracker = 0
# #! FIRST, USE A WHILE LOOP TO ITERATE THROUGH EACH ROW OF THE PATTERN.
while tracker < size:

    for i in range(size):
        print('*', end='')
    print()
    tracker += 1



#! INSIDE THE WHILE LOOP, USE A FOR LOOP TO PRINT ASTERISKS (*) SIDE BY SIDE WITHOUT ADVANCING TO A NEW LINE (YOU CAN USE PRINT("*", END="") FOR THIS).

#! AFTER COMPLETING EACH ROW, PRINT A NEWLINE CHARACTER TO MOVE TO THE NEXT ROW.
#! CONTINUE UNTIL THE PATTERN FORMS A SQUARE OF THE INPUTTED SIZE.



# EXAMPLE INTERACTION:

# IF THE USER INPUTS 4, THE OUTPUT SHOULD BE:

# ENTER THE SIZE OF THE PATTERN: 4
# ****
# ****
# ****
# ****