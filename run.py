import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os
import time
from coinmarketcap import *
import colorama
import pyfiglet
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def clear_terminal():
    """
    This will clear the terminal
    """
    os.system('clear')


def welcome_screen():
    """
    Displays a welcome message that fills the page
    """
    title = pyfiglet.figlet_format("Welcome\nTo Bank -\nWicksy", width=51)
    print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{title}')
    time.sleep(4)
    clear_terminal()


def outro_screen():
    """
    Displays a thank you message that fills up the whole page
    """
    outro_title = pyfiglet.figlet_format(
        "Thank You\nFor Using\n Bank\nWicksy", width=51)
    print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{outro_title}')
    time.sleep(4)


def validate_num(num):
    try:
        num = int(num)

    except ValueError:
        print('\n***********************************************\n')
        print(f"You entered: {num}, Please enter only numbers!")
        return False


def validate_int(num):
    """
    Will validate is the users coin amount to ensure only contains numbers
    """

    try:
        num = float(num)
        return num
        return True

    except ValueError:
        print(
            f'{Fore.RED}{Style.BRIGHT}\n------------------'
            f'--------------------------\n')
        print(f"You entered: {num}, Please enter only numbers!")
        print(
            f'{Fore.RED}{Style.BRIGHT}\n------------------'
            f'--------------------------\n')
        return False


def get_int(self):
    """
    Function that handles user input for different numbers. As long as
    the input value is determined to be an integer, it is returned.
    Otherwise, a ValueError is raised to print the message below.
    """
    while True:
        try:
            return int(input(self))

        except ValueError:
            print(f'{Fore.RED}{Style.BRIGHT}------------------------------')
            print(f"{Fore.RED}{Style.BRIGHT}\nNot an integer, try again\n")
            print(f'{Fore.RED}{Style.BRIGHT}------------------------------')


def get_str(self):
    """
    This functions checks to see if the user has entered only letters,
    if this is not the case, then it will throw a error statement and ask
    the user to type in input again until the user returns a valid input
    """

    while True:
        a = input(self).title()
        if (a.isalpha()):
            return a
        else:
            print(
                f'{Fore.RED}{Style.BRIGHT}------------------'
                f'----------------------------------------')
            print(
                f'{Fore.RED}{Style.BRIGHT}\nYou entered "{a}" '
                f'Enter only letters, no special characters\n')
            print(
                f'{Fore.RED}{Style.BRIGHT}--------------------'
                f'--------------------------------------')


class User:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def user_detials(self):
        f"Hello {self.fname} {self.lname} welcome "
        f"to our advanced banking system"


class Bank(User):  # Create a bank and will inherit from the user
    # Bank has its own attributes of total deposits and total withdrawals
    total_deposits = 0
    total_withdrawals = 0

    def __init__(self, fname, lname, age, balance):
        super().__init__(fname, lname, age)  # Gets attributes from User class
        self.balance = balance

    def balance_info(self):
        return print(
            f"{self.fname} has a remaining balance of: $ "
            f"{Fore.GREEN}{Style.BRIGHT}{self.balance}{Fore.RESET}\n")
        time.sleep(2)

    def deposit(self):
        while True:
            dp = validate_int(
                input(
                    f"{self.fname.title()} "
                    f"please enter how much you would like to deposit: $"))
            if (dp):
                print(
                    f'{Fore.GREEN}{Style.BRIGHT}'
                    f'------------------------------------')
                print(f'{Fore.GREEN}{Style.BRIGHT}Thank you for depositing...')
                print(
                    f'{Fore.GREEN}{Style.BRIGHT}'
                    f'------------------------------------')
                time.sleep(1)

                self.balance += dp
                self.total_deposits += 1
                return (
                    f"Your balance is now: "
                    f"{Fore.GREEN}{Style.BRIGHT}"
                    f"{round(self.balance, 2)}{Fore.RESET}\n")

    def withdrawals(self):
        while True:
            wd = validate_int(input(
                f"{self.fname.title()} please enter how much you "
                f"would like to withdraw: $"))
            if self.balance > wd and (wd):
                print(
                    f'{Fore.GREEN}{Style.BRIGHT}----------------------'
                    f'------------------')
                print(
                    f'{Fore.GREEN}{Style.BRIGHT}Thank you for '
                    f'withdrawing...')
                print(
                    f'{Fore.GREEN}{Style.BRIGHT}---------------'
                    f'-------------------------\n')
                self.balance -= wd
                self.total_withdrawals += 1
                return f'Your balance is now: $ {round(self.balance, 3)}\n'
                clear_terminal()
                break


investment_list = []
crypto_List = []


def get_crypto_list():
    """"
    Accumulates all the cryptocrrency name's that the api can get,
    example - Bitcoin, and stores them all in a list
    """

    for d in data['data']:
        crypto_name_from_api = d['symbol']
        crypto_List.append(crypto_name_from_api)


class crypto_portfolio(Bank):

    def __init__(self, fname, lname, age, balance):
        # Gets attributes from User class
        super().__init__(fname, lname, age, balance)

    def display_crypto_portfolio(self):
        """
        Displays a frame that contains all current
        investments the user has made into cryptocurrency
        """
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}##'
            f'#########################################################')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}##'
            f'####### Welcome to your Cryptocurrency Portfolio ########')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}##'
            f'#########################################################\n')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}***'
            f'*******************************************************')
        print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}                   ')
        for i, x in zip(range(5), investment_list):
            print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}  {i+1}  {x}')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT} '
            f'                                                       ')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT} '
            f'                                                       ')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT} '
            f'                                                       ')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT} '
            f'                                                       ')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT} '
            f'                                                       ')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT} '
            f'                                                       ')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT} '
            f'                                                       ')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT} '
            f'                                                       ')
        print(
            f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}*'
            f'*********************************************************')

    def calculate_crypto(self, crypto_info):
        """
        Calculates the price of which cryptocurrency the user wants
        and returns the amount of crypto he has invested in
        """
        price = 0
        amount = crypto_info.split('/')[0]
        coin = crypto_info.split('/')[1]
        for x in coins:
            if x['symbol'].lower() == coin.lower():
                price = float(x['quote']['USD']['price'])
        amount_of_crypto = float(amount)/price
        return print(
            f'crypto: {Fore.GREEN}{Style.BRIGHT}{coin}{Fore.RESET} '
            f'amount: {Fore.GREEN}{Style.BRIGHT}{amount_of_crypto}\n')

    def amount_to_invest(self, balance):
        """
        Ask's user how much money they would like to invest in cryptocurrency
        and which cryptocurrency they would like to invest in.
        This function also checks to see weather the user can afford the amount
        of money invested by checking the users current balance
        """
        while True:
            amount = validate_int(input(
                'How much money would you like to '
                f'invest in a crypto currency: $'))
            if amount <= self.balance and (amount):
                balance = balance - amount

                print(
                    f'\n{Fore.LIGHTBLUE_EX}{Style.BRIGHT}-'
                    f'-----------------------')
                print(f'{Fore.BLUE}{Style.BRIGHT}Processing Data......')
                print(
                    f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}--'
                    f'----------------------\n')
                time.sleep(2)
                break
            else:
                print(
                    f'{Fore.RED}{Style.BRIGHT}-'
                    f'--------------------------------------------------')
                print(
                    f'Your balance is {balance}, do '
                    f'not invest more thank your balance')
                print(
                    f'{Fore.RED}{Style.BRIGHT}----'
                    f'---------------------------------------------\n')

        while True:

            for i in range(len(crypto_List)):
                crypto_List[i] = crypto_List[i].lower()

            data = WordCompleter(crypto_List)
            crypto_type = ''
            crypto_type = prompt(
                "Enter cryptocurrency to invest in: ", completer=data)

            print(
                f'\n{Fore.LIGHTBLUE_EX}{Style.BRIGHT}--'
                f'-------------------------------')
            print(
                f'{Fore.BLUE}{Style.BRIGHT}Searching '
                f'database for coin......')
            print(
                f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}--'
                f'-------------------------------\n')
            time.sleep(2)
            if crypto_type in crypto_List:
                print('cryptocurrency found in bank...\n')
                return f'{amount}/{crypto_type}'
                break
            else:
                print(
                    'This crypto is not found in our crypto bank, '
                    'please choose another one')

    def display_values(self):

        for i in range(len(crypto_List)):
            crypto_List[i] = crypto_List[i].lower()

        data2 = (crypto_List)

        data = WordCompleter(crypto_List)
        crypto_type = ''
        while crypto_type not in data2:

            crypto_type = prompt("Enter cryptocurrency: ", completer=data)

            if crypto_type in data2:
                print(
                    f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}--'
                    f'-----------------------------------------')
                print(f'{Fore.BLUE}{Style.BRIGHT}Calculating live price')
                print(
                    f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}-'
                    f'------------------------------------------')
                time.sleep(1)
                price = 0
                crypto_type = crypto_type.upper()
                for x in coins:
                    if x['symbol'] == crypto_type:
                        price = float((x['quote']['USD']['price']))
                print(
                    f'\nThe current cost of 1 {crypto_type} = $ '
                    f'{Fore.GREEN}{Style.BRIGHT}{price}{Fore.RESET}\n')
                time.sleep(1)
                break

            else:
                print('-----------------------------------')
                print(f"{Fore.RED}{Style.BRIGHT} Invalid cryptocurrency")
                print('-----------------------------------\n')


def get_balance(fname, lname):
    while True:
        balance = validate_int(input(
            f'{fname} {lname} please enter your inital balance: £'))
        if (balance):
            balance = round(balance, 2)
            print(
                f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}--'
                f'-----------------------------------------')
            print(f'{Fore.BLUE}{Style.BRIGHT}Storing data....')
            print(
                f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}--'
                f'-----------------------------------------')
            time.sleep(2)
            print(
                f'You currently have £ {Fore.GREEN}{Style.BRIGHT}'
                f'{balance}{Fore.RESET} in your bank account\n')
            time.sleep(2)
            clear_terminal()
            return balance
            break


def main_menu():
    print(
        f'{Fore.BLUE}{Style.BRIGHT}------'
        f'------------------------------------------')
    print(
        f'{Fore.BLUE}{Style.BRIGHT}------'
        f'--- Welcome to our banking system --------')
    print(
        f'{Fore.BLUE}{Style.BRIGHT}------'
        f'------------------------------------------\n')
    print(f'{Fore.BLUE}Type the number of which option you want to access\n')
    while True:
        options_choice = get_int(
            '1) See Balance\n2) Withdraw\n3) Deposit\n4) '
            'See Total Withdraws\n5) see Total Deposits\n6) '
            'Crypto Portfolio\n7) exit\n')
        if options_choice == 1:
            clear_terminal()
            print(user_one_bank.balance_info())

        elif options_choice == 2:
            clear_terminal()
            print(user_one_bank.withdrawals())

        elif options_choice == 3:
            clear_terminal()
            print(user_one_bank.deposit())

        elif options_choice == 4:
            clear_terminal()
            print(
                f'There have been {Fore.BLUE}{Style.BRIGHT}'
                f'{user_one_bank.total_withdraws}{Fore.RESET} withdrawals.\n')

        elif options_choice == 5:
            clear_terminal()
            print(f'There have been {user_one_bank.total_deposits} deposits.')

        elif options_choice == 6:
            clear_terminal()
            crypto_menu()
            break

        elif options_choice == 7:
            clear_terminal()
            outro_screen()
            sys.exit()
        else:
            clear_terminal()
            print("Please choose a number from 1-7.")


def crypto_menu():
    print(
        f'{Fore.BLUE}{Style.BRIGHT}----'
        f'--------------------------------------------')
    print(
        f'{Fore.BLUE}{Style.BRIGHT}----'
        f'-------- Crypto Banking system -------------')
    print(
        f'{Fore.BLUE}{Style.BRIGHT}---'
        f'---------------------------------------------\n')
    print(f'{Fore.BLUE}Type the number of which option you want to access\n')
    while True:
        options_choice = get_int(
            '1) Check Crypto Portfolio\n2) Check live crypto prices\n3) '
            'Invest in crypto\n4) Exit')
        if options_choice == 1:
            clear_terminal()
            print(user_one_portfolio.display_crypto_portfolio())

        if options_choice == 2:
            clear_terminal()
            get_crypto_list()
            print(user_one_portfolio.display_values())

        if options_choice == 3:
            clear_terminal()
            get_crypto_list()
            a = (user_one_portfolio.amount_to_invest(user_one_balance))
            values = user_one_portfolio.calculate_crypto(a)
            investment_list.append(values)

        if options_choice == 4:
            clear_terminal()
            main_menu()


welcome_screen()
user_details_confirmation = ''
while True:
    if user_details_confirmation == 'yes':
        print("Thank you")
        user_one = User(fname, lname, age)
        clear_terminal()
        break
    else:
        print(
            f'{Fore.BLUE}{Style.BRIGHT}First we need to get '
            f'a few important details from you.\n')
        fname = get_str('Enter your first name: ')
        print('\n')
        lname = get_str('Enter your last name: ')
        print('\n')
        age = get_int('Enter your age: ')

        user_details_confirmation = input(
            f"\nType {Fore.GREEN}{Style.BRIGHT}'yes'"
            f"{Fore.RESET} to confirm your details\n"
            f'First name: {fname}\n'
            f'Last name {lname}\n'
            f'Age: {age}\n').lower().strip()


user_one_balance = get_balance(user_one.fname, user_one.lname)
user_one_bank = Bank(
    user_one.fname, user_one.lname, user_one.age, user_one_balance)
user_one_portfolio = crypto_portfolio(
    user_one.fname, user_one.lname, user_one.age, user_one_balance)


main_menu()
