""""
Efuah Akhimien-Mhonan
Lab 9 Exercise, Unit Testing
Feb 26, 2026
"""

import unittest
from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # default BankAccount instance before each test
        self.account = BankAccount("Efuah", 100)

    def test_initial_balance(self):
        # Test that the account is initialized with the correct balance
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit_adds_to_balance(self):
        # Test that a deposit operation correctly adds the specified amount
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw_subtracts_from_balance(self):
        # Test that a withdrawal operation correctly subtracts the specified amount
        self.account.withdraw(40)
        self.assertEqual(self.account.get_balance(), 60)

    def test_withdraw_more_than_balance_raises_exception(self):
        # Test that attempting to withdraw more than available balance raises ValueError
        with self.assertRaises(ValueError):
            self.account.withdraw(1000)

    def test_sequence_of_deposits_and_withdrawals(self):
        # Test a sequence of deposits and withdrawals to ensure correct calculations
        self.account.deposit(25)     # 100 -> 125
        self.account.withdraw(50)    # 125 -> 75
        self.account.deposit(10)     # 75 -> 85
        self.account.withdraw(5)     # 85 -> 80
        self.assertEqual(self.account.get_balance(), 80)


if __name__ == "__main__":
    unittest.main()