import unittest

from src.account import Account  # Adjust the import based on your project structure
from app.companyAccount import CompanyAccount

class TestAccountHistory:
    def test_transaction_standard_transfers(self):
        account = Account("Joe","Smith","")
        account2 = Account("Joe","Smith","")
        account.balance = 200
        account2.balance = 200

        account.transfer_money(10,account2)
        account.express_transfer(50,account2)
        account2.express_transfer(30,account)
        assert account.history == [-10,-50,-1,30]

    def test_promo_transfer(self):
        account = Account("Joe","Smith",pesel="10345678901", promo_code="PROM_110")

        assert account.history == [50]

    def test_transaction_express_transfers(self):
        account = CompanyAccount("Joe","")
        account2 = Account("Joe","Smith","")
        account.balance = 200
        account2.balance = 200

        account.transfer_money(10,account2)
        account.express_transfer(50,account2)
        account2.express_transfer(30,account)
        assert account.history == [-10,-50,-5,30]
