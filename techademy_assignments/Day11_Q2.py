import pytest

class BankApp:

    def login(self, user, password):
        if user == "Admin" and password == "admin123":
            return True
        return False

    def deposit(self, balance, amount):
        return balance + amount

    def withdraw(self, balance, amount):
        if amount <= balance:
            return balance - amount
        return "Insufficient Balance"

@pytest.fixture
def app():
    return BankApp()

def test_login(app):
    assert app.login("Admin", "admin123") == True

def test_deposit(app):
    balance = app.deposit(1000, 300)
    assert balance == 1300

def test_withdraw(app):
    balance = app.withdraw(1500, 500)
    assert balance == 1000

def test_insufficient_balance(app):
    result = app.withdraw(200, 500)
    assert result == "Insufficient Balance"
