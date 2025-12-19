from src.account import Account
from app.companyAccount import CompanyAccount

class TestAccount:

    def test_normal_email(self,mocker):
        test = mocker.patch("smtp.smtp.SMTPClient.send", return_value=True)
        self.ext_account = Account("John","Doe","321")
        self.ext_account.balance = 100
        self.ext_account.send_history_via_email("test@test.com")
        assert test.call_args[0][1] == "Personal account history: []"
        assert test.call_args[0][2] == "test@test.com"    
    def test_company_email(self,mocker):
        test = mocker.patch("smtp.smtp.SMTPClient.send", return_value=True)
        mocker.patch("app.companyAccount.CompanyAccount.is_nip_valid", return_value=True)
        self.ext_account = CompanyAccount("Test Company","1234567890")
        self.ext_account.balance = 100
        self.ext_account.express_transfer(10,None)
        self.ext_account.send_history_via_email("test@test.com")
        assert test.call_args[0][1] == "Company account history: [-10, -5]"
        assert test.call_args[0][2] == "test@test.com"
