from bank import create_account, deposit, withdraw, show_balance, view_accounts, accounts
from unittest import TestCase

class TestBank (TestCase):
        def setup(self):
                accounts.clear()

        def test_create_account(self):
                new_account = create_account("Justine", "09021887133", 21345566788, 200)
                self.assertEqual(len(accounts), 1)
                self.assertEqual(new_account[0] [0], "Justine")
                create_account("Esther", "07081726343", 2454553432322, 100.0)
                self.assertEqual(len(accounts), 2)
                self.assertIn(["Esther", "07081726343", 2454553432322, 100.0], accounts)

        def test_deposit(self):
                create_account("Esther", "07081726343", 2454553432322, 100.0)
                updated_account = deposit("Esther", 50.0)
                self.assertIsNotNone(updated_account)
                self.assertEqual(updated_account[3], 150.0)








