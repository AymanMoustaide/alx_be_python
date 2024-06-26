
#_ THIS SCRIPT WILL ASK THE USER ABOUT THE CURRENT WEATHER CONDITIONS AND PROVIDE CLOTHING RECOMMENDATIONS BASED ON THE INPUT. 
#_ THIS TASK AIMS TO DEMONSTRATE THE USE OF IF, ELIF, AND ELSE STATEMENTS TO MAKE DECISIONS IN A PROGRAM.

#* INSTRUCTIONS:

# PROMPT USER FOR WEATHER INPUT:

# ASK THE USER TO INPUT THE CURRENT WEATHER FROM A PREDEFINED SET OF CONDITIONS: “SUNNY”, “RAINY”, OR “COLD”.

weather = input("What's the weather like today? (sunny/rainy/cold):") #! Use the prompt: “What’s the weather like today? (sunny/rainy/cold): ”.


#! PROVIDE CLOTHING RECOMMENDATIONS:
#! Based on the user’s input, your program will recommend different types of clothing:

if weather == "sunny": #! If the weather is “sunny”, recommend: “Wear a t-shirt and sunglasses.”
    print('Wear a t-shirt and sunglasses.')


elif weather == 'rainy': #! If the weather is “rainy”, recommend: “Don’t forget your umbrella and a raincoat.”
    print("Don't forget your umbrella and a raincoat.")

elif weather == 'cold':  #! If the weather is “cold”, recommend: “Make sure to wear a warm coat and a scarf.
    print('Make sure to wear a warm coat and a scarf.')

else:
    print("Sorry, I don't have recommendations for this weather.") #! Include an else statement that handles unexpected input by printing: “Sorry, I don’t have recommendations for this weather.

# Output the Recommendation:

# Print the clothing recommendation based on the weather condition provided by the user.
# Example Interaction:

# What's the weather like today? (sunny/rainy/cold): sunny
# Wear a t-shirt and sunglasses.
# Or, for an unexpected input scenario:

# What's the weather like today? (sunny/rainy/cold): windy
# Sorry, I don't have recommendations for this weather.