def get_multiplication(*args):
        product = 1
        for arg in args:
                product = product * arg   
        return product


result = get_multiplication(5, 4)
print(result)

total = get_multiplication(12, 2, 3, 13, 15)
print(total)