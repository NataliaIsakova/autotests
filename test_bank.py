import pytest

from OOP import SavingsAccount, BankAccount


def test_balance_after_interest():
    acc = SavingsAccount("Анна")
    acc.deposit(500)
    acc.withdraw(100)
    acc.apply_interest()

    assert acc.get_balance() == 420

def test_withdraw_negative():
    acc = BankAccount("Анна", 100)

    with pytest.raises(ValueError):
        acc.withdraw(-50)