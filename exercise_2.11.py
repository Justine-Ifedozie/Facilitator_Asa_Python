#Exercise 2.11

first_number = int(input('Enter a five digit number: '))

first_digit = first_number // 10000

second_digit = first_number % 10000

second_digit_2 = second_digit // 1000

third_digit = second_digit % 1000

third_digit_2 = third_digit // 100

fourth_digit = third_digit % 100

fourth_digit_2 = fourth_digit // 10

fourth_digit_3 = fourth_digit_2 % 10

fiftth_digit = third_digit % 10

print(first_digit   ,second_digit_2,   third_digit_2,   fourth_digit_3,   fiftth_digit)