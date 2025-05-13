#exercise 3.9
user_number = int(input("Enter a five digit integer: "))
for counter in range (1, 6):
    first_number = user_number % 10 
    second_number = first_number // 10
    print(second_number)
