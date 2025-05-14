#exercise 3.9
user_number = int(input("Enter a five digit integer: "))


for counter in range (5):    
    
    each_digit= user_number % 10 
    user_number = user_number // 10
    
    
    #answer = each_digit + answer

    
    
    print(each_digit, end= ' ')
