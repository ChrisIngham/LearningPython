class Account:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        self.balance = self.balance + amount
        print("Deposit Accepted")

    def withdraw(self, amount):

        if (amount <= self.balance):
            self.balance = self.balance - amount
            print("Withdraw Successful")
        else:
            print("Funds Unavailable!")

acct1 = Account('Jose',100)
print(acct1.owner)
print(acct1.balance)

acct1.deposit(1000)
print(acct1.balance)
acct1.withdraw(500)
print(acct1.balance)
acct1.withdraw(10000000000000)
print(acct1.balance)