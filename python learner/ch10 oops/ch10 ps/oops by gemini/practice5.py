class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        return self.balance
    
BankAccount1 = BankAccount("Hassaan", 1000)

BankAccount1.deposit(500)
BankAccount1.withdraw(200)
print(f"{BankAccount1.owner} has {BankAccount1.balance}")
