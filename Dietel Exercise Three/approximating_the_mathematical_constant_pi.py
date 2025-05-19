denominator = 1
count = 500
pi = 0.0
alternate = 1.0

for number in range(count):
        factorial = 4.0/ denominator * alternate
        pi += factorial
        alternate *= -1
        denominator += 2
            
        print("The value of PI approximated by ", number, " term is: ", pi)  
