

# #* Prompt for a Single Task:
    
# #! ASK THE USER TO INPUT A TASK DESCRIPTION AND SAVE IT INTO A TASK VARIABLE
# task = input('TASK DESCRIPTION:')

# # ! PROMPT FOR THE TASK’S PRIORITY (HIGH, MEDIUM, LOW) AND SAVE IT INTO A PRIORITY VARIABLE
# priority = input('TASK PRIORITY:')

# #! IN A TIME_BOUND VARIABLE, ASK IF THE TASK IS TIME-BOUND (YES OR NO)
# time_bound = input('IS IT TIME-BOUND? (YES/NO):')


# #* Process the Task Based on Priority and Time Sensitivity:

# #! Use a Match Case statement to react differently based on the task’s priority.

# match priority:
#     case 'high':
#         print(f'Reminder:, {task} is a high priority task that requires immediate attention today!')
#     case 'medium':
#         print('This is a medium-priority task.')
#     case 'low':
#         print('This is a low-priority task.')


# #! Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.


# num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# count = 0
# for i, v in enumerate(num_list):
#     if v <= 50:
#         print(f'above "50"',v, i)

# print()

# for i, v in enumerate(num_list):
#     if i <= 49:
#         print(f'under 49',{v}, {i})







#_ You are going to write a program that calculates the highest score from a List of scores.

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# for n in range(0, len(student_scores)):
#     print(n)

# student_scores[n] = int(student_scores[n])



# student_scores.sort()


# print(f'The highest score in the class is:', student_scores [-1])



#// adj = ["red", "big", "tasty"]
#// fruits = ["apple", "banana", "cherry"]

# //print('Choise')
# //for x in adj:
#  // for y in fruits:
#    // print(x, y)

#     //if x == adj[0] and y == fruits[2]:
#       //print()
#       print('Choise')
#     //elif x == adj[1] and y == fruits[2]:
#       //print()
#       //print('Choise')

