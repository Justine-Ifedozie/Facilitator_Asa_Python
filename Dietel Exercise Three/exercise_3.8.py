#Arithmetic, Smallest and Largest

user_number = 0

for count in range (1, 4):
    largest = user_number
    user_number = int(input("Enter a number: "))
    
    if user_number > largest:
        largest = user_number
    
    #sum = sum + user_number
    print(largest)

   


