def get_categorized_numbers(*args, divisor = 5):
        result = ()
        count = 0
        while count < len(args):
                if args[count] % divisor == 0:
                        result = result + (args[count])
                        count+=1
                        
                if arg % divisor == 0:
                        return list(result)
                else:
                        return ("No divisible number found")

        return result

user_number1 = 10
user_number2 = 15
user_number3 = 21
user_number4 = 30
divisor = 5
get_categorized_numbers(user_number1, user_number2, user_number3, user_number4, divisor)