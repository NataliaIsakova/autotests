from OOP import SavingsAccount


def test_balance_positive():
    acc = SavingsAccount("Анна")
    acc.deposit(500)
    acc.withdraw(100)
    acc.apply_interest()

    assert acc.get_balance() > 0