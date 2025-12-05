"""
Create a mini ATM simulation (simple, text-based).

    Write a Python program that:

            Starts with a default balance = ₹10,000

            Shows a menu:
                1. Check Balance
                2. Deposit Money
                3. Withdraw Money
                4. Exit

            Perform the respective action when the user enters a choice.

            Validate inputs:

                Deposit must be > 0

                Withdrawal must be > 0 and ≤ balance

                Invalid choices should show: "Invalid Option"

                Loop until the user chooses Exit.
"""

from datetime import datetime

class MiniATM:

    def __init__(self, Balance = 10000):
        self.Balance = Balance

    def check_balance(self):
        print(f"The Balance In Your Account is ₹{self.Balance}\n")
        
    def Deposit(self, amt):
        if amt <= 0:
            print(" 🤏🤏 Some Amount Has to Be Deposited 🤏🤏\nTry Again\n")
        elif amt > 0:
            self.Balance += amt
            print(f"An Amount of ₹{amt} has been deposited into your account\nThe Present Account Balance is ₹{self.Balance}")

    def Withdrawal(self, amt):
        if amt <= 0:
            print("🤑 🤑 Enter a Valid Amount of Money That Can Be Withdrawn 🤑 🤑")
        elif amt > self.Balance:
            print("!! Insuffecient Balance !!")
        elif amt <= self.Balance:
            self.Balance -= amt
            print(f"An Amount of ₹{amt} has been withdrawn from your account\nAt ⏱️{datetime.now()}⏱️\nYour Current Account Balance is ₹{self.Balance}")
    
    def Menu_Display(self):
        User_In = input("""
______🏦 Welcome to Mini ATM 🏦______
Choose an Option from the Following Menu:-
1. Check Balance ---> B
2. Deposit Money ---> D
3. Withdraw Money --> W
4. Done Using ATM --> X
                        \n""").upper()
        return User_In
    
ATM = MiniATM() 
while True:
    X = ATM.Menu_Display()
    if X == "B":
        ATM.check_balance()
    elif X == "D":
        Amount_D = int(input("\nEnter Amount To Be Deposited(₹): \n"))
        ATM.Deposit(Amount_D)
    elif X == "W":
        Amount_W = int(input("\nEnter Amount To Be Withdrawn(₹): \n"))
        ATM.Withdrawal(Amount_W)
    elif X == "X":
        print("\n🙏🏻🙏🏻🙏🏻 Thank You For Using Mini ATM 🙏🏻🙏🏻🙏🏻\n")
        break
    
    
