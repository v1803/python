print('Welcome To MLE Bank ATM')
restart=('Y')
chances = 3
balance = 2033.33
while chances >= 0:
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (3333):
        print('You entered you pin Correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Check Account Balance\n')
            print('Please Press 2 Withdraw Cash\n')
            print('Please Press 3 To Deposit Cash\n')
            print('Please Press 4 To Take Your Card\n')
            option = int(input('Choose our Services : '))
            if option == 1:
                print('Your Balance is Rs',balance,'\n')
                restart = input('Do you want to return to homepage\n')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? \n100 Rs/200 Rs/500 Rs/1000 Rs/2000 Rs for other enter 1: '))
                if withdrawl in [100, 200, 500, 1000, 2000,]:
                    balance = balance - withdrawl
                    print ('\nYour Balance is now Rs',balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [100, 200, 500, 1000, 2000,]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Amount for Withdraw'))    

            elif option == 3:
                Pay_in = float(input('Please Enter the amount you want to deposit '))
                balance = balance + Pay_in
                print ('\nYour Balance is now Rs',balance)
                restart = input('Go to main menu ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for you service')
                break
            else:
                print('Please Enter correct Pin. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break