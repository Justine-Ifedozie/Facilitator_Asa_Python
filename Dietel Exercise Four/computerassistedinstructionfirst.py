import random

def get_computer_assisted():
        random_number = random.randint(1, 9)
        random_number2 = random.randint(1, 9)
        numbers = (random_number, random_number2)
        print("For testing: ", random_number * random_number2)

        return numbers

tuple = get_computer_assisted()    
for index, value in enumerate(tuple):
        if index == 0:
                first = value
        if index == 1:
                second = value

sentinel = 1

while sentinel != -1:
        product = int(first * second)

        user_guess = int(input(f"How much is {first} times {second} ?: "))
        if user_guess == product:
                print("Very good!") 
                tuple = get_computer_assisted()    
                for index, value in enumerate(tuple):
                        if index == 0:
                                first = value
                        if index == 1:
                                second = value

        elif user_guess != product:
                print("No. Please try again.") 
        sentinel = int(input("Enter -1 to end or any number to continue: "))
                
