'''
2. Constructor (__init__)
#The __init__ method automatically runs when you create an object.

=> Example: ATM Account Setup (When you open a bank account, your name and starting balance are added automatically.
The constructor is like that auto-setup.It runs as soon as you create a new account and fills in the basic details like your name and balance.)

=> Example Code:
------------------
# Define the class
class ATMAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def show_balance(self):
        print(self.holder_name, "has ₹", self.balance, "in the account.")

# Create object and call method
account1 = ATMAccount("Amit", 5000)         # Object created with constructor
account1.show_balance()

Output:
       Amit has ₹ 5000 in the account.
'''
