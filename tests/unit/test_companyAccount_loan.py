from src.account import CompanyAccount
import pytest

class TestCompanyAccount:

    @pytest.fixture
    def ext_account(self):
        self.ext_account = CompanyAccount("Test Company","1234567890")
        self.ext_account.balance = 100
        return self.ext_account

    def test_no_sus_loan(self,ext_account):

        self.ext_account.history= [100,-100,100]
        self.ext_account.balance += 100
        result = self.ext_account.take_loan(50)
        assert self.ext_account.balance == 200
        assert not result
    def test_too_high_loan(self,ext_account):

        self.ext_account.history= [100,-100,100,-1775]
        self.ext_account.balance += 100
        result = self.ext_account.take_loan(5000)
        assert self.ext_account.balance == 200
        assert not result
    def test_good_loan(self,ext_account):

        self.ext_account.history= [100,-100,100,-1775]
        self.ext_account.balance += 100
        result = self.ext_account.take_loan(50)
        assert self.ext_account.balance == 250
        assert result