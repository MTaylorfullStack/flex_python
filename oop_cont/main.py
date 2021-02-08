peter_parker=User("Peter", "notspidey@email.com")

peter_parker.display_user_balance()
# peter_parker.make_deposit(200).make_withdrawal(200).make_deposit(900).make_withdrawal(250)
peter_parker.display_user_balance()

spider_account=BankAccount(.02, 0)
spider_account.make_deposit(10000).make_withdrawal(100).yield_interest().display_user_balance()

peter_parker.account.make_deposit(10000).display_user_balance()