import random
list = []

def random_number_generator():
    for number in range(1,11):
        number_one = random.randint(1,50)
        list.append(number_one)
    print(list)

def get_length_of_list(list):
    count = 0
    for _ in list:
        count += 1
    return count

def sum_of_elements_in_even_position(list):
    sum = 0
    counter = 0
    for number in list:
        if counter % 2 == 0:
            sum += number
        counter += 1
    print("The sum of even elements ", sum)
    return sum

def sum_of_elements_in_odd_position(list):
    sum = 0
    counter = 0
    for number in list:
        if counter % 2 == 1:
            sum += number
        counter += 1
    print("The sum of odd elements ", sum)
    return sum

def multiply_all_elements_in_third_positions(list):
    result = 1
    counter = 1
    for number in list:
        if counter % 3 == 0:
            result *= number
        counter += 1
    return result


def average_of_all_elements_in_the_list(list):
    average = 0
    sum = 0
    for number in list:
        sum += number
    average = sum / get_length_of_list(list)
    print("The average of all elements ", average)




random_number_generator()

length = get_length_of_list(list)
print("Length of list is: ", length)

sum_of_elements_in_even_position(list)

sum_of_elements_in_odd_position(list)

result = multiply_all_elements_in_third_positions(list)
print("The product of elements in third positions: ", result)

average_of_all_elements_in_the_list(list)