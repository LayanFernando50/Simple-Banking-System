user_details = []
bank = []
bank2 = []
bank_deposite = []
bank_with = []
transfer_acc = []
transfer_money = []

text_file = open('/Users/wlaya/Desktop/practice python/2/Simple Banking System/database.txt', 'w')
new_list = user_details + bank + bank2 + bank_deposite + bank_with + transfer_acc + transfer_money
content = '\n'.join(new_list)
new_file = text_file.writelines(content)


def create_account():
    while True:
        print("1: Do you want create a account: \n"
              "2: Do you already have a account:")

        user_choice = input('Please enter the number you want: ')

        if user_choice == '1':
            user_name = input('Please enter your names: ')
            user_email = input('Please nter your email: ')
            user_pass = int(input('Please enter your password: '))

            user_details.extend([user_name, user_email, user_pass])

            print('You have successfully login')
        elif user_choice == '2':
            login_name = input('Please enter your username')
            login_pass = int(input('Please enter your password: '))

            if login_name in user_details and login_pass in user_details:
                print('Welcome to money 101')

                while True:
                    print('1: Deposite funds \n'
                          '2: Withdraw funds \n'
                          '3: Balance check \n'
                          '4: Transaction History')

                    user_input = input('Please enter a number to continue: ')

                    if user_input == '1':
                        user_dep = int(input('Please enter the amount you want deposite: '))
                        user_with_d = input('Please enter your current date')
                        print(f'You entered amount is {user_dep} {user_with_d}')
                        bank.append(user_dep)
                        bank_deposite.extend([user_dep, user_with_d])

                    elif user_input == '2':
                        user_with = int(input('Please enter the amount you want to withdraw: '))
                        user_with_w = input('Please enter your current date')
                        print(f'The amount you withdraw is {user_with} {user_with_w}')

                        bank.append(-user_with)
                        balance = sum(bank)
                        bank2.append(balance)
                        bank_with.extend([user_with, user_with_w])



                    elif user_input == '3':
                        print(f'Total balance is {sum(bank2)}')

                    elif user_input == '4':
                        print('4: Do want to see your deposite:\n'
                              '5: Do you want to see your withdrawals\n'
                              '6: Transfer\n'
                              '7: Do you want to edit info')
                        user_depo = input('Please enter your choice: ')

                        if user_depo == '4':
                            print(f'Here is your Data\n'
                                  f'{bank_deposite}')

                        elif user_depo == '5':
                            print(f'Here is your withdraw Data\n'
                                  f'{bank_with}')

                        elif user_depo == '6':

                            user_transfer = int(input('Please enter the account number: '))
                            print(f'Entered Account number is {user_transfer}')
                            sender_transfer = int(input('Please enter senders transfer number: '))
                            user_t_amount = int(input('Please enter your amount: '))
                            transfer_money.append(user_t_amount)
                            bank.append(-user_t_amount)
                            balance1 = sum(bank)
                            bank2.append(balance1)
                            print(f'Total balance is {sum(bank2)}')


                        elif user_depo == '7':
                            pre_name = input('Please enter previous name: ')

                            if pre_name in user_details:
                                new_username = input('Please enter you new user name: ')
                                user_details.remove(pre_name)
                                print(f'Your new name is {new_username}')

                            else:
                                print(f'Sorry there is no name called {pre_name}')







            else:
                print('Incorrect user or password')
        else:
            print('Invalid option')


create_account()
