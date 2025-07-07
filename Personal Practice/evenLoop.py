def even_numbers(lists):
    for number in lists:
        if number % 2 == 0:
            print(number, " is an even number")
        else:
            print(number)

even_numbers([12, 2, 3, 4, 5, 6, 7, 8, 9, 10])