# Create a class “BankAccount” with deposit & withdraw functions.							

class BankAccount:

    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0 :
            print("\nYou Need to Have Money to Deposit !!\n")
            return
        else:
            print(f"\nThe Amount ₹{amount} have been deposited into your account\n Your Current Balance is ₹{self.balance+amount}\n")
            return  
    
    def withdraw(self, amount):
        if amount <= 0:
            print("\nWithdrawal Amount should be Greater than zero '0'\n")
            return
        elif amount > self.balance:
            print( "\n₹₹ Insuffecient Balance ₹₹\n")
            return
        elif amount <= self.balance:
            print(f"\nAn Amount of ₹{amount} has been withdrawn from your account\nYour Current Balance is ₹{self.balance-amount}\n")
            return

B1 = BankAccount(100000)
B1.deposit(10000)
B1.withdraw(25000000)
B1.withdraw(40000)
    