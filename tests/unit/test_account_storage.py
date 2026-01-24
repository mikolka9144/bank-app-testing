from src.account import Account,BaseAccount
import pytest

class TestCompanyAccount:

    @pytest.fixture(autouse=True)
    def set_up(self,mocker):
        self.account1 = Account("John", "Doe", pesel='12345678901')
        self.account2 = Account("John", "Dog", pesel='10987654321')

    def test_account_packing(self):
        ext = self.account1.to_dict()
        assert ext["first_name"] == "John"
        assert ext["last_name"] == "Doe"
    def test_base_account_packing(self):
        ext = BaseAccount().to_dict()
        assert ext["balance"] == 0
        assert ext["history"] == []
    def test_base_account_depacking(self):
        ext = BaseAccount.from_dict({
            "balance":100,
            "history":[]
        })
        assert ext.balance == 100
    def test_account_depacking(self):
        ext = Account.from_dict({
            "balance":100,
            "history":[],
            "first_name":"test",
            "last_name":"Dog",
            "pesel":"Invalid"
        })
        assert ext.balance == 100