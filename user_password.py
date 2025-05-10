#User password

user_password = input("Enter your password: ")
for number in range(8, 16):

counter=0
for count in user_password:

    counter += 1
    
    if user_password < 8:
        print('Password strength is very weak')





#length_2 = (str(user_password))
#if length_2 < '8':
    #print('Password strength is very weak')
#if length_2 == '8':
    #print('Password strength is weak')
#elif length_2 > '8' and length_2 < 16:
    #print('Password strength is strong')
