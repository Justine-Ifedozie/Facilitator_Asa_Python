
class Account:
    def __init__(self, name, balance1=0):
        self.name = name
        self.balance1 = balance1

    def withdraw(self, amount):
        self.balance1 -= self.balance1
        print("Account Withdrawal")

    def deposit(self, amount):
        self.balance = self.balance1 + amount
        print("Account Deposit")

oba = Account("oba", 1500)

oba.withdraw(1500)
print(oba.balance1)

oba.deposit(1200)
print(oba.balance)
