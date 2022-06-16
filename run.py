# import colorama
# from colorama import Fore, Style


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

    def Balance_info(self):
        return f"{self.fname} has a remaining balance of: £{round(self.balance, 2)}"

    def deposit(self):
        dp = float(input(f"{self.fname.title()}, please enter how much you would like to deposit"))
        print("Thank you for depositing...")
        self.balance += dp
        self.total_deposits += 1
        return f"Your balance is now: {round(self.balance, 2)}"

    def withdraws(self):
        wd = float(input(
            f"{self.fname.title()}, please enter how much you "
            f"would like to withdraw"))
        if self.balance < wd:
            return "You can't withdraw that amount"
        else:
            print("Thank you for withdrawing...")
            self.balance -= wd
            self.total_withdraws += 1
            return f"Your balance is now: {round(self.balance, 2)}"

# class crypt portfolio:

# TODO: - display all crypto exchange rates in real time

# TODO: - ask user how much and which crypto they want to invest in

# TODO: - functions to exchange amount user wants exchanged to specific crypto

# TODO: - displays all crypto with amount invested in each crypto currency


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
    Function that handles user input for different numbers. As long as
    the input value is determined to be an integer, it is returned.
    Otherwise, a ValueError is raised to print the message below.
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


def validate_num(balance):
    """
    Will validate is the users coin amount to ensure only contains numbers
    """
    try:
        balance = float(balance)
        print(f"Amount entered is valid")

    except ValueError:
        print(f"  Amount must be a number!")


def get_balance(fname, lname):
    while True:
        balance = float(input(f'{fname} {lname} please enter your inital balance: £'))
        if (balance):
            balance = round(balance, 2)
            break
        else:
            print("\nEnter only numbers\n")

    print('-------------------------------------------')
    print('Storing data....')
    print('-------------------------------------------')
    print(f'You currently have £{balance} in your bank account\n')


def main_menu():
    print('Welcome to our advance banking system')
    print('Here are a list of what we can offer you')
    print('Type the number of which option you want to access')
    # while True:
    #     options_choice = get_int("1) See Balance\n2) Withdraw\n3) Deposit\n4) See Total Withdraws\n5) see Total Deposits\n6) Quit\n")
    #     if options_choice == 1:


user_details_confirmation = ''
while True:
    if user_details_confirmation == 'yes':
        print("Thank you")
        user_one = User(fname, lname, age)
        break
    else:
        fname = get_str("Enter your first name: ")
        lname = get_str("Enter your last name: ")
        age = get_int("Enter your age: ")
        user_details_confirmation = input(
            f"Type 'yes' to confirm your details\n "
            f"First name: {fname}\n "
            f"Last name {lname}\n "
            f"Age: {age}\n")


user_one_balance = get_balance(user_one.fname, user_one.lname)
user_one_bank = Bank(user_one.fname, user_one.lname, user_one.age, user_one_balance)
