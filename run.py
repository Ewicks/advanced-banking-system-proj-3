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
    title = pyfiglet.figlet_format("Welcome\nTo Bank -\nWicksy", width = 51)
    print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{title}')
    time.sleep(4)
    clear_terminal()


def outro_screen():
    """
    Displays a thank you message that fills up the whole page
    """
    outro_title = pyfiglet.figlet_format("Thank You\nFor Using\n Bank\nWicksy", width = 51)
    print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{outro_title}')
    time.sleep(4)

# def validate_int(self):
#     """
#     Will validate is the users coin amount to ensure only contains numbers
#     """
    
#     try:
#         amount = float(amount)
#         print(f"Amount entered is valid")
#         return True

#     except ValueError:
#         print(f"  Amount must be a number!")
#         return False


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
            print(f"\n Not an integer, try again\n")


def get_str(self):
    """

    """

    while True:
        a = input(self).title()
        if (a.isalpha()):
            return a
        else:
            print(f'\nYou entered "{a}" Enter only letters, no special characters\n')

        # try:

        # except ValueError:
        #     print(f"\n {self} , try again\n")


class User:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def user_detials(self):
        f"Hello {self.fname} {self.lname} welcome "
        f"to our advanced banking system"


class Bank(User):  # Create a bank and will inherit from the user
    # Bank has its own attributes of total deposits and total withdraws
    total_deposits = 0
    total_withdraws = 0

    def __init__(self, fname, lname, age, balance):
        super().__init__(fname, lname, age)  # Gets attributes from User class
        self.balance = balance

    def balance_info(self):
        return f"{self.fname} has a remaining balance of: £{self.balance}"

    def deposit(self):
        dp = float(input(f"{self.fname.title()}, please enter how much you would like to deposit: "))
        print("Thank you for depositing...")
        self.balance += dp
        self.total_deposits += 1
        return f"Your balance is now: {round(self.balance, 2)}"

    def withdraws(self):
        while True:
            wd = float(input(
                f"{self.fname.title()} please enter how much you "
                f"would like to withdraw: "))
            if self.balance < wd:
                print("You can't withdraw that amount")
                break
            else:
                print("Thank you for withdrawing...")
                self.balance -= wd
                self.total_withdraws += 1
                return f"Your balance is now: {round(self.balance, 2)}"
            

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
        super().__init__(fname, lname, age, balance)  # Gets attributes from User class

    
    def display_crypto_portfolio(self):
        """
        Displays a frame that contains all current
        investments the user has made
        """
        print('##############################################')
        print('###### Welcome to your Crypto Portfolio ######')
        print('##############################################\n')
        print('**********************************************************')
        print('*                                                        *')
        for i, x in enumerate(investment_list):
            print(f'*   {i+1}  {x}       *')
        print('*                                                        *')
        print('*                                                        *')
        print('*                                                        *')
        print('*                                                        *')
        print('*                                                        *')
        print('*                                                        *')
        print('*                                                        *')
        print('*                                                        *')
        print('**********************************************************')
    

    def calculate_crypto(self, crypto_info):
        """
        Calculates the price of which cryptocurrency the user wants
        and returns the amount of crypto he has invested in
        """
        amount = crypto_info.split('/')[0]
        coin = crypto_info.split('/')[1]
        for x in coins:
            if x['symbol'] == coin:
                price = float((x['quote']['USD']['price']))

        amount_of_crypto = int(amount)/price
        return f'amount: {amount_of_crypto} - crypto: {coin}'
    

    def amount_to_invest(self, balance):
        """
        Ask's user how much money they would like to invest in cryptocurrency
        and which cryptocurrency they would like to invest in.
        This function also checks to see weather the user can afford the amount
        of money invested by checking the users current balance
        """
        while True:
            amount = int(input('How much money would you like to invest in a crypto currency: $'))
            if amount < self.balance:
                balance = balance - amount

                print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}------------------------')
                print(f'{Fore.BLUE}{Style.BRIGHT}Processing Data......')
                print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}------------------------')
                time.sleep(2)
                break

            else:
                print('You have not got enough money')
                
        while True:
            crypto_type = input('which coin would you like to invest in: ').upper().strip()

            print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}------------------------')
            print(f'{Fore.BLUE}{Style.BRIGHT}Searching database for coin......')
            print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}------------------------')
            time.sleep(2)
            if crypto_type in crypto_List:
                print(' is in our crypto bank')
                return f'{amount}/{crypto_type}'
                break
            else:
                print("This crypto is not found in our crypto bank, please choose another one")


    def display_values(self):

        for i in range(len(crypto_List)):
            crypto_List[i] = crypto_List[i].lower()

        data = WordCompleter(crypto_List)
    
        crypto_type = prompt("Enter crypto coin: ", completer=data).upper()

        print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}-------------------------------------------')
        print(f'{Fore.BLUE}{Style.BRIGHT}Calculating live price')
        print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}-------------------------------------------')
        for x in coins:
            if x['symbol'] == crypto_type:
                price = float((x['quote']['USD']['price']))
        print(f'The current cost of 1 {crypto_type} is - {price}')
        time.sleep(1)
        

def get_balance(fname, lname):
    while True:
        balance = float(input(f'{fname} {lname} please enter your inital balance: £'))
        if (balance):
            balance = round(balance, 2)
            print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}-------------------------------------------')
            print(f'{Fore.BLUE}{Style.BRIGHT}Storing data....')
            print(f'{Fore.LIGHTBLUE_EX}{Style.BRIGHT}-------------------------------------------')
            time.sleep(2)
            print(f'You currently have £{balance} in your bank account\n')
            time.sleep(2)
            clear_terminal()
            return balance
            break
        else:
            print("\nEnter only numbers\n")


def main_menu():
    print(f'{Fore.BLUE}{Style.BRIGHT}------------------------------------------------')
    print(f'{Fore.BLUE}{Style.BRIGHT}--------- Welcome to our banking system --------')
    print(f'{Fore.BLUE}{Style.BRIGHT}------------------------------------------------\n')
    print(f'{Fore.BLUE}Type the number of which option you want to access\n')
    while True:
        options_choice = get_int("1) See Balance\n2) Withdraw\n3) Deposit\n4) See Total Withdraws\n5) see Total Deposits\n6) Crypto Portfolio\n7) exit\n")
        if options_choice == 1:
            clear_terminal()
            print(user_one_bank.balance_info())

        elif options_choice == 2:
            clear_terminal()
            print(user_one_bank.withdraws())

        elif options_choice == 3:
            clear_terminal()
            print(user_one_bank.deposit())

        elif options_choice == 4:
            clear_terminal()
            print(f"There have been {user_one_bank.total_withdraws} withdraws.")

        elif options_choice == 5:
            clear_terminal()
            print(f"There have been {user_one_bank.total_deposits} deposits.")

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
    print(f'{Fore.BLUE}{Style.BRIGHT}------------------------------------------------')
    print(f'{Fore.BLUE}{Style.BRIGHT}--- Crypto Banking system ---')
    print(f'{Fore.BLUE}{Style.BRIGHT}------------------------------------------------\n')
    print(f'{Fore.BLUE}Type the number of which option you want to access\n')
    while True:
        options_choice = get_int("1) Check Crypto Portfolio\n2) Check live crypto prices\n3) Invest in crypto\n4) Exit")
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
        print(f"{Fore.BLUE}{Style.BRIGHT}First we need to get a few important details from you.\n")
        fname = get_str("Enter your first name: ")
        print('\n')
        lname = get_str("Enter your last name: ")
        print('\n')
        age = get_int("Enter your age: ")

        user_details_confirmation = input(
            f"\nType 'yes' to confirm your details\n "
            f"First name: {fname}\n "
            f"Last name {lname}\n "
            f"Age: {age}\n")


user_one_balance = get_balance(user_one.fname, user_one.lname)
user_one_bank = Bank(user_one.fname, user_one.lname, user_one.age, user_one_balance)
user_one_portfolio = crypto_portfolio(user_one.fname, user_one.lname, user_one.age, user_one_balance)


main_menu()


# TODO find a way to validate numbers with dec places an use on Bank class

# TODO improve welcome screen

# TODO give user pound to dollar exchange option