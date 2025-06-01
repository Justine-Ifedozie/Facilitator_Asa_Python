from bank import create_account, deposit, withdraw, show_balance, view_accounts, accounts
from unittest import TestCase

class TestBank (TestCase):
        def setup(self):
                accounts.clear()

        def test_create_account(self):
                new_account = create_account("Justine", "09021887133", 21345566788, 100)
                self.assertEqual(len(accounts), 1)
                self.assertEqual(new_account[0] [0], "Justine")
                create_account("John", "07081726343", 2454553432322, 100.0)
                self.assertEqual(len(accounts), 2)
                self.assertIn(["John", "07081726343", 2454553432322, 100.0], accounts)

        def test_deposit(self):
                create_account("Esther", "07081726343", 2454553432322, 100.0)
                updated_account = deposit("Esther", 50.0)
                self.assertIsNotNone(updated_account)
                self.assertEqual(updated_account[3], 150.0)
                self.assertEqual(accounts[0][3], 100.0)
                result = deposit("Charlie", 40.0)
                self.assertIsNone(result)

        def test_withdraw(self):
                create_account("Evans", "07085626343", 5454553432322, 200.0)
                updated_account = withdraw("Evans", 80.0)
                self.assertIsNotNone(updated_account)
                self.assertEqual(updated_account[3], 120.0)
                self.assertEqual(accounts[0][3], 100.0)
                result_insufficient = withdraw("Evans", 300.0)
                self.assertEqual(result_insufficient, "Insufficient funds")
                result_not_found = withdraw("Jerry", 50.0)
                self.assertIsNone(result_not_found)
                self.assertEqual(accounts[0][3], 100.0)

        def test_show_balance(self):
                create_account("Mike", "09085626343", 654553432322, 200.0)
                create_account("Justice", "08085626343", 7954553432322, 300.0)
                #balance_value = show_balance("Justice")
                #self.assertEqual(balance_value, 300.0)












