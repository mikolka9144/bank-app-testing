from src.account import Account
import pytest

class TestAccount:

    @pytest.fixture
    def ext_account(self):
        self.ext_account = Account("John","Doe","321")
        self.ext_account.balance = 100
        return self.ext_account

    @pytest.mark.parametrize("history", [([100,20,100,180,100,-100]),([100,100,150,50,100,-100]),([100,100,100,100,100,-100])])
    def test_history_loan(self,ext_account,history):
        self.ext_account.history= history
        self.ext_account.balance += sum(self.ext_account.history)
        result = self.ext_account.submit_for_loan(50)
        assert self.ext_account.balance == 550
        assert result    
    def test_no_condition_loan(self,ext_account):

        self.ext_account.history= [100,-100,100]
        self.ext_account.balance += 100
        result = self.ext_account.submit_for_loan(50)
        assert self.ext_account.balance == 200
        assert not result
    def test_last_three_pay_in_loan(self,ext_account):

        self.ext_account.history= [100,100,100]
        self.ext_account.balance += 300
        result = self.ext_account.submit_for_loan(50)
        assert self.ext_account.balance == 450
        assert result