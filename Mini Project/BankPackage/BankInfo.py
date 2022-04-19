
class Account:

    def __init__(self, amt, name):
        self.amt = amt
        self.name = name


    def Deposit(self, amt):
        print(f"{amt} credited into the account")

    def Withdrawal(self, amt):
        print(f"{amt} debited fron the account")

    def __str__(self):
        return f"Amount is:{self.amt}\nName is {self.name}"

    def __eq__(self, other):
        return self.amt  == other.amt