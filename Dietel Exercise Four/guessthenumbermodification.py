import random
display = """
                Welcome
                    to
                   our
                guessing
                   game
                   """
                   
print(display)

thousand = 1000

computer_guess = random.randrange(1, thousand)
print("Hint for testing: ", computer_guess)

sentinel = int(input("Enter a number to start the game: "))

user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))

counter = 1
total = 0

while sentinel != -1:
        total = total + counter
        print("The value of thousand is: ", thousand)

        if computer_guess < user_guess:
                print("Too high. Try again")
                user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
        elif computer_guess > user_guess:
                print("Too low. Try again")
                user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
        elif computer_guess == user_guess:
                print("Congratulations. You guessed the number!")
                thousand = thousand // 2
                sentinel = int(input("Enter -1 to end the game or any other number to continue the game: "))
                if sentinel == -1:
                        print("Hint for testing: ", computer_guess)
                        if total == 10:
                                print("Either you know the secret or you got lucky!")
                                sentinel == -1
                        if total <= 10:
                                print("You should be able to do better!")
                if sentinel != -1:
                        computer_guess = random.randrange(1, thousand)
                        print("Hint for testing: ", computer_guess)
                        user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
        else:
                print("Invalid Input!")
   
print("Counter is: ", total)   
        
