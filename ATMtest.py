'''Unit test for ATM1.py

Exercise for a Test Driven Development (TDD)'''

import ATM2 as ATM
import unittest

class FirstTransaction(unittest.TestCase):    
    def test_first_deposit(self):
        '''Try a first deposit'''
        an_account = ATM.Account()
        ATM.teller(an_account, 'DEPOSIT', 100)
        self.assertEqual(100, an_account.balance)

    def test_first_withdrawal(self):
        '''Try a first withdrawal with a sufficient balance'''
        an_account = ATM.Account(200)
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


class ValidSummary(unittest.TestCase):
    summary = {'balance':0.0, 'charge':0.0, \
               'DEPOSIT':{'number':0, 'amount':0.00}, \
               'WITHDRAWAL':{'number':0, 'amount':0.00}, \
               'SERVICE_CHARGE':{'number':0, 'amount':0.00}\
               }

##    test_inputs = tuple()
##    test_outputs = tuple()

    def test_valid_summary_1(self):
        '''It should return known correct outputs with the inputs'''
        for amount in range(10, 110, 10):
            an_account = ATM.Account()
            a_summary = {'balance':float(amount), 'charge':0.0, \
                         'DEPOSIT':{'number':1, 'amount':float(amount)}, \
                         'WITHDRAWAL':{'number':0, 'amount':0.0}, \
                         'SERVICE_CHARGE':{'number':0, 'amount':0.0}\
                         }
            self.assertEqual(ATM.teller(an_account, 'DEPOSIT', amount), \
                             a_summary)

    def test_valid_summary_2(self):
        '''withdraw form 0 and deposit 100'''
##        an_account = ATM.Account()
        a_summary = {'balance':-10.0, 'charge':10.0, \
                     'DEPOSIT':{'number':0, 'amount':0.00}, \
                     'WITHDRAWAL':{'number':0, 'amount':0.00}, \
                     'SERVICE_CHARGE':{'number':1, 'amount':10.00}\
                     }
        for amount in range(10, 110, 10):
            an_account = ATM.Account()
            self.assertRaises(ATM.Overdraft, ATM.teller, \
                              *(an_account, 'WITHDRAWAL', amount))
            self.assertEqual(an_account.summary, a_summary)
            summary = {'balance':float(amount) - 10.0, 'charge':0.0, \
                       'DEPOSIT':{'number':1, 'amount':float(amount)}, \
                       'WITHDRAWAL':{'number':0, 'amount':0.00}, \
                       'SERVICE_CHARGE':{'number':1, 'amount':10.00}\
                       }
            self.assertEqual(ATM.teller(an_account, 'DEPOSIT', amount), \
                             summary)

    def test_valid_summary_3(self):
        '''balance $100 and overdraft'''
        a_summary = {'balance':90.0, 'charge':0.0, \
                     'DEPOSIT':{'number':0, 'amount':0.00}, \
                     'WITHDRAWAL':{'number':0, 'amount':0.00}, \
                     'SERVICE_CHARGE':{'number':1, 'amount':10.00}\
                     }
        for amount in range(10, 110, 10):
            an_account = ATM.Account(100)
            self.assertRaises(ATM.Overdraft, ATM.teller, \
                             *(an_account, 'WITHDRAWAL', 100 + amount))
            self.assertEqual(an_account.summary, a_summary)

class ValidTransactions(unittest.TestCase):
    '''deal a serial transactions'''
    test_1 = ( ('DEPOSIT', 100.0), ('WITHDRAWAL', 50.0) )
    test_2 = ( ('DEPOSIT', 100), ('WITHDRAWAL', 60), ('WITHDRAWAL', 60) )

    def test_transaction_1(self):
        '''Serial transaction 1'''
        an_account = ATM.Account()
        for mode, amount in self.test_1:
            ATM.teller(an_account, mode, amount)
        self.assertEqual(50.0, an_account.balance)

    def test_transaction_2(self):
        an_account = ATM.Account()
        for trans, amount in self.test_2:
            try:
                ATM.teller(an_account, trans, amount)
            except ATM.Overdraft:
                pass
        self.assertEqual((100.0 - 60 - 10), an_account.balance)

if __name__ == '__main__':
    unittest.main()
