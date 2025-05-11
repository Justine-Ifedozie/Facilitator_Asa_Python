#Exercise_2.15

first_num = float(input('Enter first number: '))

second_num = float(input('Enter second number: '))

third_num = float(input('Enter third number: '))

if first_num > second_num and third_num:
    print('The first number entered', first_num, 'is the biggest number')

if second_num > first_num and third_num:
    print('The second number entered', second_num, 'is the biggest number')

if third_num > second_num and first_num:
    print('The third ,number entered', third_num, 'is the biggest number')
