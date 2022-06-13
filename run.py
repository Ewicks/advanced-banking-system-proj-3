import colorama
from colorama import Fore, Style

class User:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def user_detials(self):
        f"Hello {self.fname} {self.lname} welcome to our advanced banking system"

class Bank(User):  # Create a bank and will inherit from the user
    # Bank has its own attributes of total deposits and total withdraws
    total_deposits = 0
    total_withdraws = 0

    def __init__(self, name, age, balance):
        super().__init__(name, age)  # Gets attributes from User class
        self.balance = balance



# class crypt portfolio:

# - display all crypto exchange rates in real time

# - ask user how much and which crypto they want to invest in

# - functions to exchange amount user wants exchanged to specific crypto

# - displays all crypto with amount invested in each crypto currency


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
                print(f"\nNot an integer, try again\n")
        


user_details_confirmation = ''
details = True
while (details):
    if user_details_confirmation == 'yes':
        print("Thank you")
        details = False
    else:
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        age = get_int("Enter your age: ")
        user_details_confirmation = input(f"Type 'yes' to confirm your details\n First name: {fname}\n Last name {lname}\n Age: {age}\n").lower()