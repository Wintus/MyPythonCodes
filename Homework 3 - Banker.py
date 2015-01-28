"""A Banker Program deals 3 types of transactions."""

def main():
    """Change the modes of trnsactions by the user inputs,
    and deal transactions."""

    balance                 = 0.0
    service_charge          = 0.0
    total_deposit           = 0.0
    total_withdrawal        = 0.0
##    total_service_charge    = 0.0

    deposit_count           = 0
    withdrawal_count        = 0
    service_charge_count    = 0

    modes = ('D', 'W', 'S', 'END')

##    def current_balance(balance):
##        try:
##            return int(balance)
##        except ValueError:
##            raise ValueError('NOT A NUMBER')

    def transaction(): #balance= 0.0, mode='D', money=0.0):
        if not mode in modes:
            raise ValueError('Wrong mode')
        if money < 0:
            raise ValueError('Negative amount')
        
        if mode == 'D':
            balance += money
            return balance
        elif mode == 'W':
            balance -= money
            if balance < 0:
                balance += money - 10
                service_charge += 10
                raise ValueError('Overdraft')
        elif mode == 'S':
            print(service_charge)
        else:
            pass

    dic_mode = {'D':"Deposit mode", 'W':"Withdrawal mode",\
                'S':"Service Charge mode", 'END':"Finished"}

    def mode_change(mode='end'):
        if not mode in modes:
            raise ValueError('Invalid mode')
        else:
            return dic_mode[mode]

    def results():
        print()
        print("Account balance: ${}".format(balance))
        print("{} deposits: total ${}".format(deposit_count, total_deposit))
        print("{} withdrawals: total ${}"\
              .format(withdrawal_count, total_withdrawal))
        print("{} service charges: total ${}"\
              .format(service_charge_count, service_charge))
        print()

    def main_process(initial_balance = 0.0):
        while True:
##            return 0

            try:        
                print("Select the modes")
                print("D: Deposit, W: Withdrawal, S: Service Charge, " + \
                      "End: finish transaction")
                mode = str(input("Mode: ")).upper() #Case-insensitive
                if mode == 'END' or '':
                    print("Finished")
                    return '__Finished__'
                else:
                    print(mode_change(mode))
                amount = float(input("Amount of the transaction: $"))
            except ValueError:
                print('Invalid input captured')
                break

            transaction()#balance, mode, amount)

            results()

    main_process()


main()
