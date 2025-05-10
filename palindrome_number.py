'''Palindrome numbers'''

user_number = int(input("Enter a five digit number: "))

first_digit = (user_number // 10000) % 100

second_digit = (user_number // 1000) % 10

third_digit = (user_number // 100) % 10

fourth_digit = (user_number // 10) % 10

fifth_digit = (user_number // 1) % 10

reversed_number =  fifth_digit, " ", fourth_digit, " ",third_digit, " ",second_digit," ", first_digit

begininng_number =  first_digit, " ", second_digit, " ",third_digit, " ",fourth_digit," ",fifth_digit


if reversed_number == begininng_number :
    print("The number you entered is a palindrome number")
else:
    print("The number you entered is not a palindrome number")
    
   