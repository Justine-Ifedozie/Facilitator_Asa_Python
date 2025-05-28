def create_account(name, phone, balance = 0.0):
        user_name = name
        user_phonenumber = phone
        account[user_name, user_phonenumber, balance]
        accounts.append(account)
        return

def show_balance():
        pass

def deposit():
        pass
        
def withdraw():
        pass
        
balance = 0
is_running = True

while is_running:
        
        welcome_text = """
Welcome to Jstee bank!
You will be required to
provide the following details:
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
                                """
        print(welcome_text)


#Driver Class
accounts = []

        customer_choice = int(input("Make a selection between 1 - 4: "))
        match customer_choice: 
                case 1: 
                        show_balance()
                case 2: 
                        deposit()
                case 3: 
                        withdraw()
                case 4:  
                        is_running = False
                case _: 
                        print("Invalid input")

print("Thank you! Have a nice day!")


                                