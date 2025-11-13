from src.account import Account


class TestAccount:

    def test_history_loan(self):
        self.ext_account = Account("John","Doe","321")
        self.ext_account.balance = 100
        self.ext_account.history= [100,100,100,100,100,-100]
        self.ext_account.balance += sum(self.ext_account.history)
        result = self.ext_account.submit_for_loan(50)
        assert self.ext_account.balance == 550
        assert result    
    def test_no_condition_loan(self):
        self.ext_account = Account("John","Doe","321")
        self.ext_account.balance = 100
        self.ext_account.history= [100,-100,100]
        self.ext_account.balance += 100
        result = self.ext_account.submit_for_loan(50)
        assert self.ext_account.balance == 200
        assert not result
    def test_last_three_pay_in_loan(self):
        self.ext_account = Account("John","Doe","321")
        self.ext_account.balance = 100
        self.ext_account.history= [100,100,100]
        self.ext_account.balance += 300
        result = self.ext_account.submit_for_loan(50)
        assert self.ext_account.balance == 450
        assert result