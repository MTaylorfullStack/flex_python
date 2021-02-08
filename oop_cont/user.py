from .bank import *

class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account=BankAccount(.02, 0)
    def display_user_balance(self):
        print(f"{self.name} has a balance of {self.account.balance}")
        return self