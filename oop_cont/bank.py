class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.count=1
        self.accounts={
            'checking': BankAccount(0, 0),
            'saving': BankAccount(.03, 200)
        }
    def create_account(self, type, int_rate, balance):
        self.accounts[type+str(self.count)] = BankAccount(int_rate, balance)
        self.count+=1
        return self


class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance-=amount
        return self
    def display_user_balance(self):
        print(f"This account has a balance of {self.balance}")
        return self
    def yield_interest(self):
        amount=self.int_rate*self.balance
        self.balance+=amount
        return self

green_goblin=User("Norman Osbourn", "goblin@gmail.com")

green_goblin.accounts['checking'].make_deposit(300).display_user_balance()

green_goblin.accounts['saving'].make_deposit(400).display_user_balance()

green_goblin.create_account('checking', 0, 500)

green_goblin.accounts['checking1'].display_user_balance()

