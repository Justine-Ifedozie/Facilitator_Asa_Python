import random
display = """
                Welcome
                    to
                   our
                guessing
                   game
                   """
                   
print(display)

computer_guess = random.randrange(1, 1001)
print("Hint for testing: ", computer_guess)

sentinel = int(input("Enter a number to start the game: "))

user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))

while sentinel != -1:
        if computer_guess < user_guess:
                print("Too high. Try again")
                user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
        elif computer_guess > user_guess:
                print("Too low. Try again")
                user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
        elif computer_guess == user_guess:
                print("Congratulations. You guessed the number!")
                sentinel = int(input("Enter -1 to end the game or any other number to continue the game: "))
                if sentinel != -1:
                        computer_guess = random.randrange(1, 1001)
                        print("Hint for testing: ", computer_guess)
                        user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
        else:
                print("Invalid Input!")

        
        
        
        