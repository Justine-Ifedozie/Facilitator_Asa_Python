number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))


def mutiplypro(number_one, number_two):
    result = 0
    
    for number in range(0, number_two):
        result = result + number_one
    return print(result)
 
mutiplypro(number_one, number_two)   