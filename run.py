import colorama
from colorama import Fore, Style

class User:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def user_detials(self):
        f"Hello {self.fname} {self.lname} welcome to our advanced banking system"





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