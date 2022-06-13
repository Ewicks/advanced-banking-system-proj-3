import colorama
from colorama import Fore, Style

class User:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def user_detials(self):
        f"Hello {self.fname} {self.lname} welcome to our advanced banking system"