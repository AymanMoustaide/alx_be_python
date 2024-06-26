import random


def guess_the_number():
    
    secret_number = random.randint(1, 2) #! Generate a secret number between 1 and 10
    print("I'M THINKING OF A NUMBER BETWEEN 1 AND 10. CAN YOU GUESS IT?")

    guess_count = 0

    while True:
        try:
            guess = int(input("ENTER YOUR GUESS: "))
        finally:
            print("PLEASE ENTER A VALID INTEGER.")
            

        guess_count += 1

        match guess:
            case _ if guess == secret_number:
                print(f"CONGRATULATIONS, YOU GUESSED IT IN {guess_count} TRIES!")
                break  #! EXIT THE LOOP IF THE GUESS IS CORRECT

            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("NOPE, YOUR GUESS IS A BIT LOW. GIVE IT ANOTHER SHOT!")

    #! PLAY AGAIN
    play_again = input("PLAY AGAIN? (YES/NO): ").lower()

    if play_again == "YES":
        guess_the_number()  #! RESTART THE GAME WITH THE WHILE LOOP
    else:
        print("THANKS FOR PLAYING! GOODBYE!")


#! CALL THE FUNCTION
guess_the_number()