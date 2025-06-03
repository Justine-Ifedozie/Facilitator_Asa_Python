from bankatmfunction import account_balance, withdraw_money, bank_account, transaction_history

account_bal = 0
withdraw_amount = 0
withdraw_fee = 100
bal_after = 0
rem_bal = 0



welcome = """
Welcome to Simulation Bank!
________________________________
You are required to make a selection:
Enter your account balance.
Withdraw money 
   Note - withdrawals must be multiples 
          of $500 or $1000 only.      
View transaction history.
________________________________
                """
print(welcome)

account_bal = int(input("Enter your account balance: $"))
print("Your current balance is: $", account_balance(account_bal))


start = True
while start:

        withdraw_amount = int(input("Enter withdrawal amount multiples of $500 or $1000: $"))
        if withdraw_amount > 20000:
                print("Failed! Enter an amount lesser than $20,000")
                withdraw_amount = int(input("Enter withdrawal amount multiples of $500 or $1000: $"))

        else:
                if bank_account[0] + 100 > withdraw_amount:
                        bal_after = withdraw_money(withdraw_amount)
                        rem_bal = bal_after - withdraw_fee
                        bank_account.append(rem_bal)
                        print("Transaction successful!")
                        print("Withdrawal fee: $", withdraw_fee)
                        print("Remaining Balance: $", rem_bal)
                else:
                        print("You entered a withdrawal amount that is higher than your balance")

        sentinel = int(input("Do you want to make another withdrawal ? 0 for yes/ any number for no: ")) 
        if sentinel == 0:
                start = False
        else:
                start = True
                
print("Your transaction history is ", transaction_history)
    
print("Thank you! Have a nice day!")
