class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else: raise ValueError('ошибочка')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else: raise ValueError('ошибочка')

    def get_balance(self):
        return self.__balance



class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.05

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        self._BankAccount__balance -= amount

acc = SavingsAccount("Анна")

acc.deposit(500)
acc.withdraw(100)
acc.apply_interest()

print(acc.get_balance())