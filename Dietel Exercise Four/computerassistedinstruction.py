import random

def get_computer_assisted():
        random_number = random.randint(1, 9)
        random_number2 = random.randint(1, 9)
        numbers = (random_number, random_number2)
        print("For testing: ", random_number * random_number2)

        return numbers

sentinel = True
while sentinel:
        tuple = get_computer_assisted()    
        for index, value in enumerate(tuple):
                if index == 0:
                        first = value
                if index == 1:
                        second = value

        product = int(first * second)
        stopper = 1
        user_guess = int(input(f"How much is {first} times {second} ?: "))
        if user_guess == product:
                good_response =         """
1.  Very good!
2.  Nice work!
3.  Keep up the good work!
                                                        """
                print(good_response)
                response_1 = int(input("Select response: "))
                match response_1:
                        case 1: 
                                print("Very good!")            
                        case 2: 
                                print("Nice work!") 
                        case 3: 
                                print("Keep up the good work!") 
                        case _: 
                                print("Invalid Input!")
        elif user_guess != product:
                good_response =         """
1.  No. Please try again.
2.  Wrong. Try once more.
3.  No. Keep trying.
                                                        """
                print(good_response)
                response_2 = int(input("Select response: "))
                match response_2:
                        case 1: 
                                print("No. Please try again.")            
                        case 2: 
                                print("Wrong. Try once more.") 
                        case 3: 
                                print("No. Keep trying.") 
                        case _: 
                                print("Invalid Input!")
 
        stopper = int(input("Enter -1 to end or any number to continue: "))
        if stopper == -1:
             sentinel = False
                