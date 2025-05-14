#exercise_3.16
largest = 0
second_largest = 0

for number in range(10):
    user_number = int(input("Enter a number: "))
    if user_number > largest:
        second_largest = largest
        largest = user_number

    elif user_number > second_largest:
        user_number = second_largest
    
print("The largest number entered is: ", largest)
print("The second largest number entered is: ", second_largest)