def modify_elements(items):
        for index in range(len(items)):
                items[index] = items[index] * 2




numbers = [20, 10, 13, 64, 75, 8, 9, 34]
modify_elements(numbers)

print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)

new_number = sorted(numbers)

print(new_number)

print(new_number.index(20))






