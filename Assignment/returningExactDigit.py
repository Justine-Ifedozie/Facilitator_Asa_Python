user_number = 0

user_number = int(input("Enter an integer: "))
if user_number < 1 or user_number > 10000:
    print("Invalid number! Enter an integer between 1 and 10,000")


def returning_sum(user_number):
    base_number = 0
    add = 0

    while user_number  != 0:
        base_number = user_number % 10
        add = add + base_number
        user_number = user_number // 10
        return add

print(returning_sum(user_number))