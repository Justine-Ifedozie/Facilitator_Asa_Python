factorial = 1
count = 10

exponential = 1
for number in range(1, count, 1):
        factorial *= number
        exponential += (1/ factorial)
            
print("The sum at 10th term is: ", exponential)  