'''Unit test for ATM1.py

Exercise for a Test Driven Development (TDD)'''

import ATM2 as ATM
import unittest

class FirstTransaction(unittest.TestCase):    
    def test_first_deposit(self):
        '''Try a first deposit'''
        an_account = ATM.Account()
##        an_account.deposit(100)
        ATM.teller(an_account, 'DEPOSIT', 100)
        self.assertEqual(100, an_account.balance)

    def test_first_withdrawal(self):
        '''Try a first withdrawal with a sufficient balance'''
        an_account = ATM.Account(200)
##        an_account.withdrawal(100)
        ATM.teller(an_account, 'WITHDRAWAL', 100)
        self.assertEqual((200 - 100), an_account.balance)

    def test_overdraft_from_zero(self):
        '''Try a withdrawal with a empty balance'''
        an_account = ATM.Account()
        self.assertRaises(ATM.Overdraft, ATM.teller, \
                          *(an_account, 'WITHDRAWAL', 100))

    def test_end_transaction(self):
        '''teller itself should accept 'END' command'''
        an_account = ATM.Account()
        self.assertRaises(ATM.FinishTransaction, ATM.teller, \
                          *(an_account, 'END'))


class InvalidTransaction(unittest.TestCase):
    def test_negative_deposit(self):
        '''It should fail with negative deposits'''
        an_account = ATM.Account()
        self.assertRaises(ATM.NegativeDeposit, ATM.teller, \
                          *(an_account, 'DEPOSIT', -100))

    def test_negative_balance(self):
        '''It should return NegativeBalanceError getting negative balances'''
        an_account = ATM.Account()
        self.assertRaises(ATM.NegativeWithdrawal, ATM.teller, \
                          *(an_account, 'WITHDRAWAL', -100))

    def test_overdraft(self):
        '''It should return Overdraft and charge a service fee'''
        an_account = ATM.Account()
        self.assertRaises(ATM.Overdraft, ATM.teller, \
                          *(an_account, 'WITHDRAWAL', 100))
        self.assertEqual(an_account.last_transaction(), ('SERVICE_CHARGE', 10))


class InvalidInput(unittest.TestCase):
    def test_invalid_operation(self):
        '''teller() should fail with invalid operation'''
        an_account = ATM.Account()
        self.assertRaises(ATM.InvalidOperation, ATM.teller, \
                          *(an_account, 'A', 'MONEY'))

    def test_non_number(self):
        '''teller() should fail with non-number amount'''
        an_account = ATM.Account()
        self.assertRaises(ATM.InvalidAmount, ATM.teller, \
                          *(an_account, 'DEPOSIT', 'MONEY'))


class ValidOutput(unittest.TestCase):
    test_inputs = tuple()
    test_outputs = tuple()

    def valid_output(self):
        '''It should return known correct outputs with the inputs'''

class ValidTransactions(unittest.TestCase):
    '''deal a serial transactions'''
    test_t_1 = (('__deposit__', 100.0), ('__withdrawal__', 50.0))

    def transaction_1(self):
        '''Serial transaction 1'''

if __name__ == '__main__':
    unittest.main()
