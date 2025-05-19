decimal_value = 0
power = 0

user_number = input("Enter a binary number in ones and zeros: ")

for bit in reversed(user_number):
        if bit == "1":
                decimal_value += 2 ** power
        elif bit != "0":
                print("Invalid input")
        
        power += 1
print(f' The decimal value of the number you entered is: {decimal_value}')