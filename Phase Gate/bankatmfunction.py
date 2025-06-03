bank_account = []

transaction_history = []

def account_balance(user_bal):
        bank_account.append(user_bal)
        transaction_history.append(user_bal)
        return bank_account[0]
        
def withdraw_money(withdraw):
        remaining_bal = bank_account[0] - withdraw
        bank_account.append(remaining_bal)
        transaction_history.append(remaining_bal)
        return remaining_bal 







