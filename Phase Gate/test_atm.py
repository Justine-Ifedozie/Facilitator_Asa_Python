from bankatmfunction import account_balance, withdraw_money, bank_account
from unittest import TestCase

class TestATM (TestCase):

        def test_that_account_balance_function_works(self):
                updated_balance = account_balance(2000)
                self.assertIsNotNone(updated_balance)

        def test_that_withdraw_money_function_works(self):
                updated_account = withdraw_money(1500)
                self.assertIsNotNone(updated_account)
                result_insufficient = withdraw_money(2000)
                
                
                
                
                
                