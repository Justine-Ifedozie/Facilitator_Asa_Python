accounts = []

def create_account(name, phone, account_number, balance = 0.0):
        account = [name, phone, account_number, balance]
        accounts.append(account)
        return accounts

def deposit(name, amount):
        for account in accounts:
                if account[0] == name:
                        account[3] += amount
                        return account
        
def withdraw(name, amount):
        for account in accounts:
                if account[0] == name:
                        account[3] = account[3] - amount
                        return account
        
        
def show_balance(name):
        for account in accounts:
                if account[0] == name:
                        print(f'Your account balance is: ${account[3]}')

def view_accounts():
        print(accounts)

is_running = True
while is_running:
        
        welcome_text = """
Welcome to Jstee bank!
_______________________
You will be required to
make a selection:
1. Create account
2. Deposit Funds
3. Withdraw
4. Show balance
5. View accounts in the bank
0. Exit
_______________________
                                """
        print(welcome_text)


#Driver Class
        import random

        customer_choice = int(input("Make a selection between 1 - 4: "))
        match customer_choice: 
                case 1: 
                        user_name = input("Enter your name: ")
                        user_phonenumber = input("Enter your phone number: ")
                        user_account_number = random.randint(1230000000, 50000000000000)
                        create_account(user_name, user_phonenumber, user_account_number, balance = 0.0)
                        print("New Account Number: ", user_account_number)
                        #print(accounts)
                case 2: 
                        account_name = input("Enter the name of the account you wish to make a deposit into: ")
                        amount = int(input("Enter deposit amount: "))
                        deposit(account_name, amount)
                        #print(accounts)
                case 3: 
                        account_user = input("Enter the name of the account you wish to withdraw from: ")
                        withdraw_amount = int(input("Enter withdraw amount: "))
                        withdraw(account_user, withdraw_amount)
                        #print(accounts)
                case 4: 
                        account_name_2 = input("Enter the name of the account you wish to view its balance: ")
                        show_balance(account_name_2)
                case 5: 
                        view_accounts()
                case 0:  
                        is_running = False
                case _: 
                        print("Invalid input")

print("Thank you! Have a nice day!")


                                