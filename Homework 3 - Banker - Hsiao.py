def main():

    intDepositNum = 0
    intWithdrawNum = 0
    intServiceNum = 0
    fltDeposit = 0.0
    fltWithdrawal = 0.0
    fltService = 0.0
    fltTotal = 0.0
    # END = "End"

    print("Welcome to our ATM")
    print("___________________")
    print("Account Summary ")
    print("Your current balance: $0.00")
    print("Your current service charges: $0.00")
    print()

    strEnd = str(input("Type 'End' in amount of transaction to exit. Continue?  ")).upper()

    while True: # strEnd != END:
        if strEnd == "END" or "NO":
            print("Your balance is: ",fltTotal)
            print("Thank you for using our ATM!")
            break

        fltTransactions = str(input("What is the amount of transaction? ")).upper()

        if fltTransactions == "END":
            print("Your balance is: ",fltTotal)
            print("Thank you for using our ATM!")
            break

        strTransactionType = str(input("Would you like to [d]eposit, [w]ithdrawal, or show [s]ervice charges? ")).lower()

        if strTransactionType == "d":
            fltTotal += fltTransactions
            intDepositNum += 1
            print("You have deposited",fltTransactions)
            print("Your balance is:",fltTotal)
            print("You have deposited",intDepositNum,"times.")


        elif strTransactionType == "w":
            if fltTransactions > fltTotal:
                fltTotal -= 10
                intServiceNum += 1
                print("You have exceeded the amount you can withdraw. There will be a $10 charge to your account")
            fltTotal -= fltTransactions
            intWithdrawNum += 1
            print("You have withdrew",fltTransactions)
            print("Your balance is:",fltTotal)
            print("You have withdraw",intWithdrawNum,"times.")

        elif strTransactionType == "s":
            print("You have been charged",intServiceNum,"times.")

        elif strTransactionType == "End":
            print("Your balance is: ",fltTotal)
            print("Thank you for using our ATM!")
            break


main()
