class BankAccount:

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if not (isinstance(amount, float) or isinstance(amount, int)):
            raise ValueError("Ongeldig bedrag")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not (isinstance(amount, float) or isinstance(amount, int)):
            raise ValueError("Ongeldig bedrag")
        self.balance -= amount
        return self.balance

    def getBalance(self):
        return self.balance

rekening = BankAccount("Jakke")
print(rekening.deposit(1.265865))
print(rekening.deposit(1.265865))
print(rekening.deposit(1.265865))
print(rekening.deposit(1.265865))
print(rekening.withdraw(8.888888888888888888))
print(rekening.owner)
print(rekening.getBalance())