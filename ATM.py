# creating a new class
# principles of object  oriented programming
# the parenthesis are optional

class Bank:
    name = "Equity"

class ATMCard(Bank):
    color = "Brown"
    balance = 0
#   this is a property
#   a class variable/ data member
# a class variable is shared  among all instances of class

# actions are called methods
# methods are just functions, only that they are inside a class
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance < amount:
            print("Sorry Insufficient funds")
        else:
            self.balance -= amount
            print("Success:{}".format(amount))
