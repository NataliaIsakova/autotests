class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.05

    def apply_interest(self):
        balance = self.get_balance()
        if balance <= 0:
            return
        interest = balance * self.interest_rate
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        self._balance -= amount


acc = SavingsAccount("Анна")
acc.deposit(500)
acc.withdraw(100)
acc.apply_interest()

print(acc.get_balance())