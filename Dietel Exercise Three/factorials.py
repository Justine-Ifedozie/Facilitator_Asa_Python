#Exercise_3.13
user_input = int(input("Enter a nonnegative integer: "))

result = 1

for counter in range(user_input, 0, -1):
    result *= counter
print("The factorial of the number you entered is: ", result)