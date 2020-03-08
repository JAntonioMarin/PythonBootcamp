class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Account owner: Jose
    # Account balance: $100
    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: {self.balance}"

    def deposit(self, money):
        if money > 0:
            self.balance = self.balance + money
            print('Deposit Accepted')
        else:
            print('Deposit Not Accepted')

    def withdraw(self, money):
        if money <= self.balance:
            self.balance = self.balance - money
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


acct1 = Account('Jose', 100)

print(acct1)

print(acct1.owner)

print(acct1.balance)

acct1.deposit(50)

print(acct1)

acct1.withdraw(75)

print(acct1)

acct1.withdraw(500)

print(acct1)
