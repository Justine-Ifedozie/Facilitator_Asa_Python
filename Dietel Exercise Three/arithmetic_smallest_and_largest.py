#Arithmetic, Smallest and Largest

user_number = int(input("Enter a number: "))
    
largest = user_number
smallest = user_number
sum = user_number
product =1;

for count in range (1, 4):
    user_number = int(input("Enter a number: "))

        
    if user_number > largest:
        largest = user_number
    if user_number < smallest:
        smallest = user_number
    sum+= user_number
    product *= user_number

print("Sum : ", sum)
average = sum / 4
print("Average : ", average)
print("Product : ", product)
print("Smallest Number : ", smallest)
print("Largest Number : ", largest)


    

   


