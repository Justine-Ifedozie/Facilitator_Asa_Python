factorial = 1
count = 10

pi = 0.0
for number in range(1, count, 1):
        factorial *= number
        pi -= (4/ factorial)
            
        print("The value of PI approximated by ", number, " term is: ", pi)  
