print("WELCOME TO KISHOREGANJ BANK ATM")
restart = 'Y'
chances = 3
balance = 15000.0

while chances >= 0:
    pin = int(input('Please Enter Your Pin: '))
    if(pin == 1234):
        while restart not in ('n', 'NO', 'no', 'N'):

            print("Welcome  Md Redawnauzzaman\n")
            print('Press 1 For Balance Inquiry')
            print('Press 2 For Withdraw')
            print('Press 3 To Credit Balance')
            print('Press 4 To Exit\n')

            pressed = int(input("Choose Your Option: "))

            if pressed == 1:
                print('Your Balance is BDT: ', balance, '\n')
                restart = input("Would You Like To Do More Transactions?\nPress (Y) to Continue, (N) to Exit ")
                if restart in ('n', 'no', 'N', 'NO'):
                    print("THANK YOU\n")
                    break

            elif pressed == 2:
                withdraw = float(input("Enter The Amount You Want to Withdraw: "))
                if withdraw > balance:
                    print("Insufficient Balance !")
                    restart = 'Y'
                else:
                    balance -= withdraw
                    print("Your New Balance: ", balance)

                restart = input("Would You Like To Do More Transactions?\nPress (Y) to Continue, (N) to Exit ")
                if restart in ('n', 'no', 'N', 'NO'):
                    print("THANK YOU\n")
                    break

            elif pressed == 3:
                credit = float(input("Enter The Amount You Would Like to Credit: "))
                balance = balance + credit
                print("Your New Balance is: ", balance)

                restart = input("Would You Like To Do More Transactions?\nPress (Y) to Continue, (N) to Exit ")
                if restart in ('n', 'no', 'N', 'NO'):
                    print("THANK YOU\n")
                    break

            elif pressed == 4:
                print("THANK YOU FOR BANKING WITH US")
                break;

            else:
                print("Please Choose a Valid Option: ")
                restart = 'Y'

    elif pin != (1234):
        print("Incorrect Pin\n")
        chances -= 1
        if chances == 0:
            print("Sorry, Session Limit Exceeds")
            break
