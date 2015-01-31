"""Checking Account Program"""

class NegativeBalance(ValueError): pass
class NegativeDeposit(ValueError): pass
class NegativeWithdrawal(ValueError): pass
class InvalidOperation(ValueError): pass
class InvalidAmount(ValueError): pass
class Overdraft(Exception): pass
class ServiceChargeRequest(Exception): pass
class FinishTransaction(Exception): pass

class Account():
    '''bank account contains current balance and all histories of transactions'''
   
    def __init__(self, init_balance=0.00, init_charge=0.00): #initialize
        if init_balance < 0 or init_charge < 0:
            raise InvalidAmount('Negative initial amount')
        self.balance = init_balance #NegativeBalance later
        self.charge = init_charge
        self.service_fee = 10.00
        
        self.transaction_history = [] #(transaction_type, its_amount)

        self.summary = {'balance':self.balance, 'charge':self.charge, \
                        'DEPOSIT':{'number':0, 'amount':0.00}, \
                        'WITHDRAWAL':{'number':0, 'amount':0.00}, \
                        'SERVICE_CHARGE':{'number':0, 'amount':0.00}\
                        }

    def last_transaction(self):
        '''return the last transaction'''
        return self.transaction_history[-1]

    def update(self, mode, amount):
        """update the transaction history

    mode = 'DEPOSIT' | 'WITHDRAWAL' | 'SERVICE_CHARGE'"""

        item = (mode, amount)
        self.transaction_history.append(item)
        self.summary['balance'] = self.balance
        self.summary['charge'] = self.charge
        self.summary[mode]['number'] += 1
        self.summary[mode]['amount'] += amount

##    def history(self, mode='TOTAL'):
##        if mode == 'TOTAL':
##            return self.transaction_history
##        elif mode in self.modes:
##            #return the list of the type of transaction
##            return [(t, v) for (t, v) in self.transaction_history \
##                    if t == mode]
        
    def sub(self, a, b):
        if a == b:
            a, b = 0, 0
        elif a > b:
            a, b = a - b, 0
        elif a < b:
            a, b = 0, b - a
        else:
            pass
        return a, b

    def checker(self, transaction, amount):
        '''check the transaction and the amount'''

    def deposit(self, amount):
        '''make a deposit, if still is charge, auto-paid'''
        if amount < 0.00:
            raise NegativeDeposit('Invalid Negative Deposit')
        elif 0 < self.charge:
            re_amount, self.charge = self.sub(amount, self.charge)
        else:
            pass
        self.balance += amount
        self.update('DEPOSIT', amount)
        
    def withdrawal(self, amount):
        '''make a withdrawal with overdraft'''
        if amount < 0.00:
            raise NegativeWithdrawal('Invelid Negatilve Withdrawal')
        elif amount > self.balance: #overdraft
            balance, service_charge = \
                     self.sub(self.balance, self.service_fee)
            self.balance -= self.service_fee
            self.charge += service_charge
            self.update('SERVICE_CHARGE', self.service_fee)
            raise Overdraft('Insufficient balance & service fee charged')
        else:
            self.balance -= amount
            self.update('WITHDRAWAL', amount)

##    def pay(self, amount):
##        '''pay for the service charge
##    Automatically paid in deposit'''

            
def teller(account, mode='END', amount=0.0): #Process
    '''deals transactions of given mode and amount

    return account summary'''
    modes = ('DEPOSIT', 'WITHDRAWAL', 'SERVICE_CHARGE', 'END')

    if not (mode in modes):
        raise InvalidOperation('Invalid operation of transaction')
    elif mode == 'END':
        raise FinishTransaction('Successfully finished')

    try:
        try:
            amount = round(float(amount), 2)
        except ValueError:
            raise InvalidAmount
    
        if mode == 'DEPOSIT':
            account.deposit(amount)
        elif mode == 'WITHDRAWAL':
            account.withdrawal(amount)
##        elif mode == 'SERVICE_CHARGE':
##            raise ServiceChargeRequest
        else:
            pass
##            raise Exception('UNKNOWN_ERROR')

    except NegativeDeposit:
        raise NegativeDeposit

    except NegativeWithdrawal:
        raise NegativeWithdrawal
    
    except Overdraft:
        raise Overdraft

    return account.summary
        

def interface(account, input_string='END'): #I/O
    '''deals with user inputs and display the outputs

    'D' -> deposit | 'W' -> withdrawal
        do transactions with entered amounts
    'S' -> service charge viewer | 'END' -> finish transaction'''

    modes = {'D':'DEPOSIT', 'W':'WITHDRAWAL', \
             'S':'SERVICE_CHARGE', 'END':'END'}

    def get_input():
        '''promts and gets the types and amounts'''
        t_type = str(input('> Enter the type of transaction: ')).upper()
        if not (t_type in modes):
            raise InvalidOperation
        print('>', modes[t_type])
        if t_type == 'END':
            raise FinishTransaction('User quit')
        elif t_type == 'S':
            raise ServiceChargeRequest
        else:
            try:
                amount = float(input('> Enter the amount of transaction: '))
                print()
            except ValueError:
                raise InvalidAmount
            return modes[t_type], amount
    
    def show_output(summary):
        '''display the summary generated by teller()'''
        width = 40
        digits = 12
        fill = '-'
        print("Account Summary".center(width + digits))
        print("Your current balance: ".ljust(width, fill) + \
              " ${:,.2f}".format(summary['balance']).rjust(digits, fill)
              )
        print("Your current service charge: ".ljust(width, fill) + \
              " ${:,.2f}".format(summary['charge']).rjust(digits, fill)
              )
        print()

        for (name, mode) in (('Deposit', 'DEPOSIT'), \
                             ('Withdrawal', 'WITHDRAWAL'), \
                             ('Service charge', 'SERVICE_CHARGE')
                             ):
            print("Total number of {}: ".format(name).ljust(width, fill) + \
                  " {}".format(summary[mode]['number']).rjust(digits, fill)
                  )
            print("The dollar amount of {}: ".format(name).ljust(width, fill) + \
                  " ${:,.2f}".format(summary[mode]['amount']).rjust(digits, fill)
                  )
            print()

    #Entrance prompt
    print("Welcome. Select the transaction types of:")
    print("D: Deposit | W: Withdrawal" + \
          " | S: Show service charges | END: end transaction.")
    print("Then enter the amount of the transaction.")
    print()
    show_output(account.summary) #display current balance and so on
    
    while True:
        try:
            show_output(teller(account, *get_input()))
            
        except Overdraft:
            print('OVERDRAFT')
            print("You don't have sufficient balane to withdraw.")
            print("Service fee $10 was charged.")
            print()
            show_output(account.summary)

        except ServiceChargeRequest:
            print("Number of charge: {}"\
                  .format(account.summary['SERVICE_CHARGE']['number']))
            print("Amount of charge: {:,.2f}"\
                  .format(account.summary['SERVICE_CHARGE']['amount']))
            print()
            show_output(account.summary)
        
        except InvalidOperation:
            print("Transaction Error: Invalid type of transaction\n")

        except InvalidAmount:
            print("Transaction Error: Invalid amount\n")

        except FinishTransaction:
            print("Your deal was finished. Thank you.\n")
            break

if __name__ == '__main__':
    an_account = Account()
    interface(an_account)
