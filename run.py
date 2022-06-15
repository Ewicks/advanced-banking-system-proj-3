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

    def __init__(self, fname, age, balance):
        super().__init__(fname, age)  # Gets attributes from User class
        self.balance = balance

    def show_info(self):
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


user_details_confirmation = ''
details = True
while (details):
    if user_details_confirmation == 'yes':
        print("Thank you")
        details = False
    else:
        fname = get_str("Enter your first name: ")
        lname = get_str("Enter your last name: ")
        age = get_int("Enter your age: ")
        user_details_confirmation = input(
            f"Type 'yes' to confirm your details\n "
            f"First name: {fname}\n "
            f"Last name {lname}\n "
            f"Age: {age}\n").lower()

# while ()

